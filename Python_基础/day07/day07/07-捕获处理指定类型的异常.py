"""
程序异常处理
学习目标：能够捕获指定类型的异常，防止程序异常导致意外终止
"""

"""
捕获一种指定类型的异常
try:
    可能发生异常的代码
except 异常类型:
      处理异常的代码
"""

# print('************************* 示例1 *************************')

# try:
#     print('============')
#     # FileNotFoundError
#     f = open('xxx.txt', 'r')
#     print('============')
# except FileNotFoundError:
#     print('try里的代码发生了FileNotFoundError异常')


# try:
#     print('============')
#     # ZeroDivisionError
#     num = 10 / 0
#     print('============')
# except ZeroDivisionError:
#     print('try里的代码发生了ZeroDivisionError异常')

"""
捕获多种指定类型的异常
try:
    可能发生异常的代码
except (异常类型1, 异常类型2):
      处理异常的代码

"""

print('************************* 示例2 *************************')


try:
    print('============')
    # FileNotFoundError
    # f = open('xxx.txt', 'r')
    # ZeroDivisionError
    num = 10 / 0
    print('============')
except (FileNotFoundError, ZeroDivisionError):
    print('try里的代码发生了FileNotFoundError或ZeroDivisionError异常')