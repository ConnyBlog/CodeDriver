# from PythonFunc import my_func
#
# print(my_func(-99))
#
# print(my_func('-99'))


# from PythonFunc import userMove
# import math
#
# x,y = userMove(100, 100, 60, math.pi / 6)
# print(x, y)


# from PythonFunc import power
# print(power(2, 3))
# print(power(2))



# from PythonFunc import enroll
# print(enroll('Bob', 'M'))
# print()
# print(enroll('Bob', 'M', 7))
# print()
# print(enroll('Bob', 'M', city='TianJin'))


# from PythonFunc import add_end
# print(add_end())
# print(add_end(None))
# print(add_end(['1','2']))


# from PythonFunc import calc
# num = calc([1, 2, 3, 4, 5])
# print(num)


# from PythonFunc import calc
#
# num = calc()
# print(num)
#
# num = calc(1, 2, 3)
# print(num)
#
# nums = [1, 2, 3]
# num = calc(*nums)
# print(num)



# from PythonFunc import person
#
# user = person('Michael', 30)
# print(user)
#
# user = person('Michael', 30, city='Beijing')
# print(user)
#
# user = person('Michael', 30, gender='M', job='Engineer')
# print(user)
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# user = person('Jack', 24, city=extra['city'], job=extra['job'])
# print(user)
#
# # **extra表示把extra这个dict的所有keyValue用关键字参数传入函数内部的**kw，kw将获得一个dict，深拷贝；
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# user = person('Jack', 24, **extra)
# print(user)
#
# user = person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
# print(user)
#
# user = person('Jack', 24, city='Beijing', job='Engineer')
# print(user)

# user1 = person('Jack', 24, city='Beijing', job='Engineer')
# # user2 = person('Jack', 24, 'Beijing', 'Engineer')
# user2 = person('Jack', 24, job='Engineer')
# print(user1, user2)




# from PythonFunc import f1
# from PythonFunc import f2

# f = f1(1,2)
# print(f)
#
# f = f1(1,2,c=3)
# print(f)
#
# f = f1(1, 2, 3, 'a', 'b')
# print(f)
#
# fNumber1 = f1(1, 2, 3, 'a', 'b', x = 99)
# fNumber2 = f1(1, 2, 3, 'a', 'b', x = 99)
# print(fNumber1, fNumber2)
#
# f = f2(1, 2, d=99, ext = None)
# print(f)

# # 通过Tuple和Dict也可以调用函数
# args = (1, 2, 3, 4)
# kw = {'d' : 9999, 'x' : '#'}
# print(f1(*args, **kw))
# print(f1(args, kw))
#
# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# print(f2(*args, **kw))
# # print(f2(args, kw))



# from recursiveFunc import fact

# print(fact(1))
# print(fact(3))
# print(fact(5))

#栈溢出
# print(fact(999))


#递归的练习
from recursiveFunc import move
action = move(3, 'A', 'B', 'C')


