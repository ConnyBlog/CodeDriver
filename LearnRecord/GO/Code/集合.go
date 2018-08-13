
package main

import "fmt"

func main() {
   // Map 集合通过hash实现
   
   // 声明变量 默认map是nil 
   // var map_variable map[key_data_type] value_data_type
   // 通过make函数创建
   // map_variable := make(map[key_data_type] value_data_type)

   // 创建集合
   var countryCaptialMap map[string] string
   countryCaptialMap = make(map[string] string)
   // 给map插入key-value
   countryCaptialMap["France"] = "Paris"
   countryCaptialMap["Italy"] = "Rome"
   countryCaptialMap["Japan"] = "Tokyo"
   countryCaptialMap["India"] = "New Delhi"
   // 打印map
   for country := range countryCaptialMap {
      fmt.Println("capital of", country, "is", countryCaptialMap[country])
   }
   //判断是否存在某个元素
   capital, ok := countryCaptialMap["United States"]
   if ok {
      fmt.Println("Cap")
   }

}