package main

import "fmt"

type Books struct {
   title string
   author string
   subject string
   book_id int
}


func main() {
   // 结构体的使用
   var Book1 Books
   var Book2 Books

   Book1.title = "Go"
   Book1.author = "RunTime"
   Book1.subject = "Ielts"
   Book1.book_id = 123

   Book2.title = "Python"
   Book2.author = "RunTime"
   Book2.subject = "GRE"
   Book2.book_id = 456

   // /* 打印 Book1 信息 */
   // fmt.Printf( "Book 1 title : %s\n", Book1.title)
   // fmt.Printf( "Book 1 author : %s\n", Book1.author)
   // fmt.Printf( "Book 1 subject : %s\n", Book1.subject)
   // fmt.Printf( "Book 1 book_id : %d\n", Book1.book_id)

   // /* 打印 Book2 信息 */
   // fmt.Printf( "Book 2 title : %s\n", Book2.title)
   // fmt.Printf( "Book 2 author : %s\n", Book2.author)
   // fmt.Printf( "Book 2 subject : %s\n", Book2.subject)
   // fmt.Printf( "Book 2 book_id : %d\n", Book2.book_id)



   // 结构体作为函数参数
   // printBook(Book1)
   // printBook(Book2)


   // 结构体作为指针
   printPtrBook(&Book1)
   printPtrBook(&Book2)
}


// func printBook( tempBook Books) {
//    fmt.Printf( "Method Book title : %s\n", tempBook.title)
//    fmt.Printf( "Method Book author : %s\n", tempBook.author)
//    fmt.Printf( "Method Book subject : %s\n", tempBook.subject)
//    fmt.Printf( "Method Book book_id : %d\n", tempBook.book_id)
// }

func printPtrBook( book *Books ) {
   fmt.Printf( "Book title : %s\n", book.title);
   fmt.Printf( "Book author : %s\n", book.author);
   fmt.Printf( "Book subject : %s\n", book.subject);
   fmt.Printf( "Book book_id : %d\n", book.book_id);
}