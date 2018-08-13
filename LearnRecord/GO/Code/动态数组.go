package main

import "fmt"

func main(){
	// 切片
	// s := [] int {1,2,3}
	// s := arr[:]
	// q := arr[0:1]
	// p := arr[0:]
	// s := arr[:2]
	// t := arr[0:1]
	// ss := make( []int, len, cap)



	// 切片的相关函数
	// var numbers = make([]int, 3, 10)
	// printSlice(numbers)



	// 空切片
	// var numbers []int
	// printSlice(numbers)

	// if (numbers == nil) {
	// 	fmt.Printf("numbers = nil \n")
	// }



	// 切片的截取
	// numbers := []int{0,1,2,3,4,5,6,7,8}   
	// printSlice(numbers)
	// fmt.Println("numbers ==", numbers)
 //    fmt.Println("numbers[1:4] ==", numbers[1:4])
 //    fmt.Println("numbers[:3] ==", numbers[:3])
 //    fmt.Println("numbers[4:] ==", numbers[4:])
   
 //    numbers1 := make([]int,0,5)
 //    printSlice(numbers1)
   
 //    number2 := numbers[:2]
 //    printSlice(number2)

 //    number3 := numbers[2:5]
 //    printSlice(number3)



    // 切片的相关操作
    var numbers [] int
    printSlice(numbers)

    numbers = append(numbers, 0)
    printSlice(numbers)

	numbers = append(numbers, 1)
	printSlice(numbers)

    numbers = append(numbers, 2,3,4)
	printSlice(numbers)

   	// 创建切片 numbers1 是之前切片的两倍容量
	numbers1 := make( []int, len(numbers), cap(numbers)*2 )
	printSlice(numbers1)

	// 拷贝 numbers 的内容到 numbers1
   	copy(numbers1,numbers)
   	printSlice(numbers1)
}


func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}