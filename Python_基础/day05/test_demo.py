"""
综合1
"""
# num = [1,1,2,3,4,4,5]
# c = [i for i in num if i % 2 != 0]
# print(c)
# print(set(num))
'''
    综合2:用列表推导式求出100以内4的倍数：
'''
# my_list = [i for i  in range(0,101) if i % 4 == 0]
# print(my_list)

'''
    综合3:输出 9*9 乘法口诀表
'''

# for i in  range(1,10):
#     for j in range(1,i+1)  :
#         print(f'{i}*{j}={i*j}',end=' ')
#     print()

'''
    综合2;使用匿名函数，实现调用一个函数处理加减乘除。(不需要考虑被除数为 0 的情况。)
        - 定义四个匿名函数实现加、减、乘、除运算
        - 定义一个函数接收 两个数字 和 匿名函数，并使用匿名函数来处理两个数字
        - 在函数中调用匿名函数，输出运算结果
        **提示: 函数的参数是可以传入另一个函数名的**
'''
_sum=lambda a,b:a+b
res = _sum(1,2)
print(res)

_sub = lambda a,b:a-b
res = _sub(1,2)
print(res)

chu = lambda a,b:a/b
res = chu(4,1)
print(res)

cheng = lambda a,b:a*b
res = cheng(3,6)
print(res)