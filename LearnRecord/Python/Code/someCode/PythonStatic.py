#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print absolute value of an integer:

# a = 100
# if a >= 0:
#     print(a)
# else:
#     print(-a)


# print('I\'m ok.')
#
# print('I\'m learning\nPython.')

# print('\t')
#
# print(r'\\\t\\')

# -*- coding: utf-8 -*-
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
#
# print ("test:", n, f, s1, s2, s3, s4)



# print('包含中文asdasdasd')
#
# a = ord('A')
# print(a)
#
# a = ord('中')
# print(a)
#
# a = chr(66)
# print(a)
#
# a = chr(25991)
# print(a)
#


# 纯英文的string可以用ASCII编码为bytes  包含中文的string可以用UTF-8编码为bytes
# 带b前缀的单引号或双引号 bytes类型的数据
#
# print(b'ABC')
# print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))
#

# 读取字节流并进行解码
# print(b'ABC'.decode('ascii'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 如果bytes包含无法解码的字节，会报错
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))

# 忽略错误进行解码
# print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))



# a = 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
# print(a)


# s1 = 72
# s2 = 85
# r = (s2-s1)/s1 * 100
# print('sco:%d %%' % r)



# 数组
# classmates = ['Michael', 'Bob', 'Tracy']
# print(classmates)
# print(len(classmates))
# print(classmates[0])
# print(classmates[1])
# print(classmates[2])
# print(classmates[-1])
# print(classmates[-2])
# print(classmates[-3])
#
# classmates.append('YUECHEN111')
# print(classmates)
#
# classmates.insert(0, 'YUECHEN222')
# print(classmates)
#
# classmates.pop()
# print(classmates)
#
# classmates.pop(0)
# print(classmates)
#
# classmates[0] = 'Sarah'
# print(classmates)


# L = ['Apple', 123, True]
# print(L)
#
# s = ['python', 'java', ['asp', 'php'], 'scheme']
# print(s,len(s))



# 元组
# classmates = ('Michael', 'Bob', 'Tracy')
# print(classmates)


# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])
