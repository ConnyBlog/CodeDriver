
package main

import "fmt"

func main() {
   // Go指针

   // var a int = 10
   // fmt.Printf("变量的地址: %x\n", &a  )


   // var a int= 20   /* 声明实际变量 */
   // var ip *int        /* 声明指针变量 */

   // ip = &a  /* 指针变量的存储地址 */

   // fmt.Printf("a 变量的地址是: %x \n", &a )

   // /* 指针变量的存储地址 */
   // fmt.Printf("ip 变量储存的指针地址: %x \n", ip )
   // /* 使用指针访问值 */
   // fmt.Printf("*ip 变量的值: %d \n", *ip )


   // var pEmpty *int
   // fmt.Printf("空指针 指针地址: %x \n", pEmpty )

   // if pEmpty == nil {
   //    fmt.Printf("空指针判断 指针地址: %x \n", pEmpty )
   // }

   // if ip != nil {
   //    fmt.Printf("空指针判断 指针地址: %x \n", ip )
   // }



   // 指针数组
   // a := []int{10,100,200}

   // for i := 0; i < 3; i++ {
   //    fmt.Printf("a [%d] = %d\n", i, a[i] )
   // }


   // a := []int{10, 100, 200}

   // var ptr [3] * int 
   // for i := 0; i < 3; i++ {
      // ptr[i] = &a[i] /* 整数地址赋值给指针数组 */
   // }
   // for j := 0; j < 3; j++ {
   //    fmt.Printf("a[%d] = %d\n", j,*ptr[j] )
   // }



   // 指向指针的指针
   // var a int
   // var ptr * int
   // var pptr ** int
   
   // a = 300
   // ptr = &a
   // pptr = &ptr

   // fmt.Printf("a = %d \n",a)
   // fmt.Printf("*ptr = %d \n",*ptr)
   // fmt.Printf("**pptr = %d \n",**pptr)



   // 指针作为函数的参数
   /* 定义局部变量 */
   var a int = 100
   var b int= 200
   fmt.Printf("交换前 a 的值 : %d\n", a )
   fmt.Printf("交换前 b 的值 : %d\n", b )

   /* 调用函数用于交换值
   * &a 指向 a 变量的地址
   * &b 指向 b 变量的地址
   */
   swap(&a, &b);

   fmt.Printf("交换后 a 的值 : %d\n", a )
   fmt.Printf("交换后 b 的值 : %d\n", b )
}


func swap(x *int, y *int) {
   var temp int
   temp = *x // temp存储 x地址的值
   *x = *y // y的值传递给x
   *y = temp // 将temp传递给y
}