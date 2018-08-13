// package main

// import "fmt"

// func main() {

// 	const LENGTH int = 10
//    	const WIDTH int = 5   
//    	var area int
//    	const a, b, c = 1, false, "str" //多重赋值

//    	area = LENGTH * WIDTH
//    	fmt.Printf("面积为 : %d", area)
//    	println()  
//    	println(a, b, c)
// }

// package main

// import "unsafe"

// const (
//     a = "abc"
//     b = len(a)
//     c = unsafe.Sizeof(a)
// )

// func main() {
//     println(a, b, c)
// }


// package main

// import "fmt"

// func main() {
//     const (
//             a = iota   //0
//             b          //1
//             c          //2
//             d = "ha"   //独立值，iota += 1
//             e          //"ha"   iota += 1
//             f = 100    //iota +=1
//             g          //100  iota +=1
//             h = iota   //7,恢复计数
//             i          //8
//     )
//     fmt.Println(a,b,c,d,e,f,g,h,i)
// }


// package main

// import "fmt"

// import "unsafe"

// const (
// 	i = 1 << iota
// 	j = 3 << iota
// 	k
// 	l
// )

// func main() {
// 	fmt.Println("i=",i)
// 	fmt.Println("j=",j)
// 	fmt.Println("k=",k)
// 	fmt.Println("l=",l)


// 	var a = "hello"
// 	const b = unsafe.Sizeof(a)
// 	println(a, b)
// }



// 算术运算

// package main

// import "fmt"

// func main() {

//    var a int = 21
//    var b int = 10
//    var c int

//    c = a + b
//    fmt.Printf("第一行 - c 的值为 %d\n", c )
//    c = a - b
//    fmt.Printf("第二行 - c 的值为 %d\n", c )
//    c = a * b
//    fmt.Printf("第三行 - c 的值为 %d\n", c )
//    c = a / b
//    fmt.Printf("第四行 - c 的值为 %d\n", c )
//    c = a % b
//    fmt.Printf("第五行 - c 的值为 %d\n", c )
//    a++
//    fmt.Printf("第六行 - c 的值为 %d\n", a )
//    a--
//    fmt.Printf("第七行 - c 的值为 %d\n", a )
// }



// 关系运算

// package main

// import "fmt"

// func main() {

//    var a int = 21
//    var b int = 10

//    if( a == b ) {
//       fmt.Printf("第一行 - a 等于 b\n" )
//    } else {
//       fmt.Printf("第一行 - a 不等于 b\n" )
//    }
   
//    if ( a < b ) {
//       fmt.Printf("第二行 - a 小于 b\n" )
//    } else {
//       fmt.Printf("第二行 - a 不小于 b\n" )
//    } 
   
//    if ( a > b ) {
//       fmt.Printf("第三行 - a 大于 b\n" )
//    } else {
//       fmt.Printf("第三行 - a 不大于 b\n" )
//    }


//    a = 5
//    b = 20
   
//    if ( a <= b ) {
//       fmt.Printf("第四行 - a 小于等于 b\n" )
//    }
//    if ( b >= a ) {
//       fmt.Printf("第五行 - b 大于等于 a\n" )
//    }
// }



// 逻辑运算

// package main

// import "fmt"

// func main() {

//    var a bool = true
//    var b bool = false
   
//    if ( a && b ) {
//       fmt.Printf("第一行 - 条件为 true\n" )
//    } else {
//       fmt.Printf("第一行 - 条件为 false\n" )
//    }
   
//    if ( a || b ) {
//       fmt.Printf("第二行 - 条件为 true\n" )
//    } else {
//       fmt.Printf("第二行 - 条件为 false\n" )
//    }
   
//    a,b = !a,!b
   
//    if ( a && b ) {
//       fmt.Printf("第三行 - 条件为 true\n" )
//    } else {
//       fmt.Printf("第三行 - 条件为 false\n" )
//    }
   
//    if ( !(a && b) ) {
//       fmt.Printf("第四行 - 条件为 true\n" )
//    } else {
//       fmt.Printf("第四行 - 条件为 false\n" )
//    }
// }


// package main

// import "fmt"

// func main() {

//    var a uint = 60    /* 60 = 0011 1100 */  
//    var b uint = 13    /* 13 = 0000 1101 */
//    var c uint = 0          

//    c = a & b       /* 12 = 0000 1100 */ 
//    fmt.Printf("第一行 - c 的值为 %d\n", c )

//    c = a | b       /* 61 = 0011 1101 */
//    fmt.Printf("第二行 - c 的值为 %d\n", c )

//    c = a ^ b       /* 49 = 0011 0001 */
//    fmt.Printf("第三行 - c 的值为 %d\n", c )

//    c = a << 2     /* 240 = 1111 0000 */
//    fmt.Printf("第四行 - c 的值为 %d\n", c )

//    c = a >> 2     /* 15 = 0000 1111 */
//    fmt.Printf("第五行 - c 的值为 %d\n", c )
// }


// package main

// import "fmt"

// func main() {
//    var a int = 21
//    var c int

//    c =  a
//    fmt.Printf("第 1 行 - =  运算符实例，c 值为 = %d\n", c )

//    c +=  a
//    fmt.Printf("第 2 行 - += 运算符实例，c 值为 = %d\n", c )

//    c -=  a
//    fmt.Printf("第 3 行 - -= 运算符实例，c 值为 = %d\n", c )

//    c *=  a
//    fmt.Printf("第 4 行 - *= 运算符实例，c 值为 = %d\n", c )

//    c /=  a
//    fmt.Printf("第 5 行 - /= 运算符实例，c 值为 = %d\n", c )

//    c  = 200; 

//    c <<=  2
//    fmt.Printf("第 6行  - <<= 运算符实例，c 值为 = %d\n", c )

//    c >>=  2
//    fmt.Printf("第 7 行 - >>= 运算符实例，c 值为 = %d\n", c )

//    c &=  2
//    fmt.Printf("第 8 行 - &= 运算符实例，c 值为 = %d\n", c )

//    c ^=  2
//    fmt.Printf("第 9 行 - ^= 运算符实例，c 值为 = %d\n", c )

//    c |=  2
//    fmt.Printf("第 10 行 - |= 运算符实例，c 值为 = %d\n", c )

// }



// package main

// import "fmt"

// func main() {
//    var a int = 4
//    var b int32
//    var c float32
//    var ptr *int

//    /* 运算符实例 */
//    fmt.Printf("第 1 行 - a 变量类型为 = %T\n", a );
//    fmt.Printf("第 2 行 - b 变量类型为 = %T\n", b );
//    fmt.Printf("第 3 行 - c 变量类型为 = %T\n", c );

//    /*  & 和 * 运算符实例 */
//    ptr = &a    /* 'ptr' 包含了 'a' 变量的地址 */
//    fmt.Printf("a 的值为  %d\n", a);
//    fmt.Printf("*ptr 为 %d\n", *ptr);
// }




// 优先级	运算符
// 7		^ !
// 6		* / % << >> & &^
// 5		+ - | ^
// 4		== != < <= >= >
// 3		<-
// 2		&&
// 1		||

package main

import "fmt"

func main() {
   var a int = 20
   var b int = 10
   var c int = 15
   var d int = 5
   var e int;

   e = (a + b) * c / d;      // ( 30 * 15 ) / 5
   fmt.Printf("(a + b) * c / d 的值为 : %d\n",  e );

   e = ((a + b) * c) / d;    // (30 * 15 ) / 5
   fmt.Printf("((a + b) * c) / d 的值为  : %d\n" ,  e );

   e = (a + b) * (c / d);   // (30) * (15/5)
   fmt.Printf("(a + b) * (c / d) 的值为  : %d\n",  e );

   e = a + (b * c) / d;     //  20 + (150/5)
   fmt.Printf("a + (b * c) / d 的值为  : %d\n" ,  e );  
}

