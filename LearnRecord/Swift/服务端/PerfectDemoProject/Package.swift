//软件包管理
import PackageDescription

let package = Package(
    name: "PerfectTemplate",
    targets: [],
    dependencies: [
        //HTTP服务
        .Package(url: "https://github.com/PerfectlySoft/Perfect-HTTPServer.git", majorVersion: 2, minor: 0),
        
        //MySQL服务
        .Package(url: "https://github.com/PerfectlySoft/Perfect-MySQL.git", majorVersion: 2, minor: 0),
        
        //Mustache
        .Package(url: "https://github.com/PerfectlySoft/Perfect-Mustache.git", majorVersion: 2, minor: 0),
        
        //Request日志过滤器
//        .Package(url: "https://github.com/dabfleming/Perfect-RequestLogger.git", majorVersion: 0),
        
        //日志写入文件
//        .Package(url: "https://github.com/PerfectlySoft/Perfect-Logger.git", majorVersion: 0, minor: 0)
    ]
)
