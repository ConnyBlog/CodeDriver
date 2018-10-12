import PerfectLib
import PerfectHTTP
import PerfectHTTPServer
import PerfectMustache

//1
//print("HELLO WORLD~~~~~~")

//2
//func handler(data: [String:Any]) throws -> RequestHandler {
//    return {
//        request, response in
//        response.setHeader(.contentType, value: "text/html")
//        response.appendBody(string: "<html><title>Hello, world!</title><body>Hello, world!</body></html>")
//        response.completed()
//    }
//}
//
//let confData = [
//    "servers": [
//        [
//            "name":"localhost",
//            "port":8181,
//            "routes":[
//                ["method":"get", "uri":"/", "handler":handler],
//                ["method":"get", "uri":"/**", "handler":PerfectHTTPServer.HTTPHandler.staticFiles,
//                 "documentRoot":"./webroot",
//                 "allowResponseFilters":true]
//            ],
//            "filters":[
//                [
//                    "type":"response",
//                    "priority":"high",
//                    "name":PerfectHTTPServer.HTTPFilter.contentCompression,
//                    ]
//            ]
//        ]
//    ]
//]
//
//do {
//    try HTTPServer.launch(configurationData: confData)
//} catch {
//    fatalError("\(error)")
//}

//3
// 创建服务
let server = HTTPServer()

// 创建路由
var route = Routes()

// 路由链接配置
route.add(method: .get, uri: "/login") { (request, response) in
    response.appendBody(string: "/login Hello Perfect ~ This is get ~")
    response.completed()
}

route.add(method: .post, uri: "/login") { (request, response) in
    
    guard let username = request.param(name: "userName") else {
        return;
    }
    guard let password = request.param(name: "password") else {
        return;
    }
    
    let responsDic : [String : Any] = ["result" : "SUCCESS" , "responsBody" : ["userName":username,"password":password]]
    do {
        let json = try responsDic.jsonEncodedString()
        response.setBody(string: json)
    } catch {
        response.setBody(string: "ERROR")
    }
    
    response.completed()
}

// 动态
let valueKey = "key"
route.add(method: .get, uri: "/path1/{\(valueKey)}/detail") { (request, response) in
    response.appendBody(string: "/path1 test ~ The string in this path is : \(request.urlVariables[valueKey]!)")
    response.completed()
}

// 通配符
route.add(method: .get, uri: "/path2/*/detail") { (request, response) in
    response.appendBody(string: "/path2 test ~ The string in this path is : \(request.path)")
    response.completed()
}

route.add(method: .get, uri: "/path3/**") { (request, response) in
    response.appendBody(string: "/path3 test ~ The string in this path is : \(request.urlVariables[routeTrailingWildcardKey]!)")
    response.completed()
}

// 添加路由配置
server.addRoutes(route)
// 设置端口
server.serverPort = 8888
server.documentRoot = "./webroot"


/// Mustache
struct TestHandler : MustachePageHandler {
    //句柄必须继承 MustachePageHandler
    //当句柄需要将参数传入模版时 被系统调用
    // - 参数 context 上下文环境
    //   MustacheWebEvaluationContext 程序内读取HTTPRequest请求内容而保存的所有信息
    // - 参数 collector 结果查找器
    //   MustacheEvaluationOutputCollector 调整模版输出
    func extendValuesForResponse(context contxt: MustacheWebEvaluationContext, collector: MustacheEvaluationOutputCollector) {
        var values = MustacheEvaluationContext.MapType()
        values["title"] = "Swift"
        
        contxt.extendValues(with: values)
        
        do {
            try contxt.requestCompleted(withCollector: collector)
        } catch {
            let response = contxt.webResponse
            response.status = .internalServerError
            response.appendBody(string: "\(error)")
            response.completed()
        }
    }
}
//对index进行重定向 将index交给句柄处理
route.add(method: .get, uri: "/") { (request, response) in
    let webRoot = request.documentRoot
    mustacheRequest(request: request, response: response, handler: TestHandler(), templatePath: webRoot + "/index.html")
}



/// 日志系统
//let logPath = "./files/log"
//let dir = Dir(logPath)
//if dir.exists == false {
//    try Dir(logPath).create()
//}


//configureServer(server)

do {
    try server.start()
} catch PerfectError.networkError(let err, let msg) {
    print("Network error thrown: \(err) \(msg)")
}

