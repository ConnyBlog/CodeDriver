# 递归函数
# 递归函数需要防止函数溢出。函数的调用是通过栈这种数据结构实现的，进入一个函数，栈就会加一层栈帧，当函数返回，栈就会减一层帧；
# 由于栈的大小不是无限的，所以调用次数过多就会出现栈溢出；
# 解决栈溢出：尾递归优化，循环是特殊的尾递归函数；


# #计算阶乘
# def fact(n):
#     print('n=',n)
#     if n == 1:
#         return 1
#     return n * fact(n-1)


# 尾递归优化
# 函数返回的时候，调用自身本身，并且return不能包含表达式，这样编译器可以把尾递归做优化，无论递归本身调用多少次都只占用1个帧；

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 练习
# 汉诺塔的移动可以用递归函数非常简单地实现。
#
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
# -*- coding: utf-8 -*-
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c);
    else:
         move(n-1, a, c, b)
         move(1, a, b, c)
         move(n-1, b, a, c)
