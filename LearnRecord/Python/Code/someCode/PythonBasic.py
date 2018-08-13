#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 条件判断
# age = 20
# if age >= 18:
#     print('age is ', age)
#     print('adult')
# else:
#     print('age is ', age)
#     print('teenager')

# age = 3
# if age < 8:
#     print('age is ', age)
#     print('kid')
# elif age >= 18:
#     print('age is ', age)
#     print('adult')
# else:
#     print('age is ', age)
#     print('teenager')



# 条件判断
# age = 20
# if age >= 18:
#     print('age is ', age)
#     print('adult')
# else:
#     print('age is ', age)
#     print('teenager')

# age = 3
# if age < 8:
#     print('age is ', age)
#     print('kid')
# elif age >= 18:
#     print('age is ', age)
#     print('adult')
# else:
#     print('age is ', age)
#     print('teenager')


# if age:
#     print('True')



# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')



# height = 1.73
# weight = 70.0
#
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print('过轻')
# elif bmi < 25:
#     print('正常')
# elif bmi < 28:
#     print('过重')
# elif bmi < 32:
#     print('肥胖')
# else:
#     print("严重肥胖")



# 循环语句

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)



# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)



# Range函数  生成一个正数序列
# List函数  转化为一个List
# print(list(range(5)))


# sum = 0
# for x in range(100):
#     sum += x
#     print(x , sum)
#
# print(sum)


# sum = 0
# n = 99
# while n > 0:
#     sum = sum+n
#     n = n-2
# print(sum)



# L = ['Lisa', 'Adam', 'Bart', 'Beta']
# for n in L :
#     print(n)


# n = 1
# while n <= 100:
#     print(n)
#     n = n + 1
# print('END')


# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')


# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)



# 死循环
# number = 100;
# n = 0;
# while n < number:
#     print(n, number)
#     n += 1;
#     if n == 99:
#         n = 0



# dic = {'A':'100', 'B':'99', 'C':'70'}
# print(dic)
#
#
# if 'B' in dic:
#     print(dic['B'])
#
# if dic.get('U'):
#     print(dic['A'])
#
# dic.pop('A')
# print(dic)


# set 无重复数据、无顺序的集合
# s = set([1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5])
# print(s)
# s.add(6)
# s.add(6)
# print(s)
# s.remove(6)
# print(s)

# set 不可以保存可变数据
# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([3, 4, 5, 6, 7, 8])
# print(s1 | s2)
# print(s1 & s2)


# 可变和不可变
# a = ['a', 'c', 'b', 'e', 'd']
# a.sort()
# print(a)
#
# b = 'abc'
# c = b.replace('a', 'A')
# print(b)
# print(c)












