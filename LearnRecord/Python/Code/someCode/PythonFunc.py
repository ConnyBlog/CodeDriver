#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


# a = abs(100)
# print(a)
#
# b = abs(-30)
# print(b)
#
# c = abs(12.34567)
# print(c)
#
#
# d = max(1, 2, 3, 4, 5, 100, 999, 879)
# print(d)



# e = int('123')
# f = int(12.345678)
# g = float('12.345678')
# h = str(1.23456)
# i = bool(1)
# j = bool(0)
#
# print(e, f, g, h, i, j)


# n1 = 255
# n2 = 10086
# print(hex(n1), hex(n2))


# def my_func(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x



# def nop():
#     pase



# def userMove(x, y, step, angle = 0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny



# def power(x):
#     return x*x;


# def power(x, n=2):
#     s = 1;
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s




# def enroll(name, gender, age=6, city='Beijing'):
#     print(name)
#     print(gender)
#     print(age)
#     print(city)
#     return



# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L



# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum


# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum


# # 关键字参数
# # 允许传入0个或任意个含参数名的参数，这些关键字内部自动组装为一个Dict
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)


# 命名关键字参数
# 如果要限制关键字参数的名字，可以用命名关键字参数；特殊分隔符*，*后面的参数被认为是命名关键字参数
# def person(name, age, *, city, job):
#     print(name, age, city, job)

# # 函数中已经定义一个可变参数，后面跟着的命名关键字不需要特殊分隔符*
# def person (name, age, *args, city='Beijing', job):
#     print(name, age, args, city, job)
#
# # 如果没有*作为特殊分隔符，Python解释器无法识别位置参数和命名关键字参数
# def person(name, age, city, job):
#     # 缺少 *，city和job被视为位置参数
#     pass





# 函数可以用 必选参数、默认参数、可变参数、关键字参数、命名关键字参数
# 顺序必须是：必须按、默认、可变、命名关键字、关键字
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)




# 关于函数
# *args是可变参数，接受一个Tuple
# 可变参数可以直接传入，func(1, 2, 3)，也可以组装list或tuple再通过*args传入，fuc(*(1, 2, 3))
# **kw是关键字参数，接受一个Dict
# 关键字参数可以直接传入，func(a=1, b=2)，也可以组装dict，再通过**tw传入， func(**{'a':1, 'b':2})







