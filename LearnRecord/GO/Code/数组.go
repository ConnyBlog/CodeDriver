package main

import "fmt"

func main() {
   var n [10] int /* n 是一个长度为 10 的数组 */
   var i,j int

   /* 为数组 n 初始化元素 */         
   for i = 0; i < 10; i++ {
      n[i] = i + 100 /* 设置元素为 i + 100 */
   }

   /* 输出每个数组元素的值 */
   for j = 0; j < 10; j++ {
      fmt.Printf("Element[%d] = %d\n", j, n[j] )
   }


   /* 多维数组 - 5 行 2 列*/
   var a = [5][2]int{ {0,0}, {1,2}, {2,4}, {3,6},{4,8}}
   var x, y int

   /* 输出数组元素 */
   for  x = 0; x < 5; x++ {
      for y = 0; y < 2; y++ {
         fmt.Printf("a[%d][%d] = %d\n", x, y, a[x][y] )
      }
   }

   /* 形参未设定数组大小 */
   var balance = []int {1000, 2, 3, 17, 50}
}



func getAverage(arr []int, size int) float32 {
	var i int
	var avg,sum float32

	for i = 0; i < count; i++ {
		sum += arr[i]
	}

	avg = sum / size
	return avg
}
