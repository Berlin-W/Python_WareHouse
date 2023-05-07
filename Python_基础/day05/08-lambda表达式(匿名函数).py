"""
lambda表达式：简单函数的简洁写法

lambda [形参1], [形参2], ... : [单行表达式] 或 [函数调用]

注意：
1）匿名函数中不能使用 while 循环、for 循环，只能编写单行的表达式，或函数调用
2）匿名函数中返回结果不需要使用 return，表达式的运行结果就是返回结果
3）匿名函数中也可以不返回结果。例如： lambda : print('hello world')
"""


# def func_sum(a, b):
#     """
#     计算a，b的和，返回结果
#     """
#     return a + b
#  写一个 lambda 表达式(匿名表达式)
func = lambda a,b: a + b  # a + b 是返回值
print(type(func))
result = func(2,4)
print(result)




