# 定义一个内置变量:__all__  来限定from 模块名 import *时导入那些内容
# __all__ = ['字符串']
__all__ = ['num','my_sum','my_sub']


# 定义一个变量
num = 10
# 定义一个函数,计算两个数字的和
def my_sum(a,b):
    '''计算两个数的和'''
    return a + b


# 定义一个函数,计算两个函数的差
def my_sub(a,b):
    '''计算两个数字的差'''
    return  a - b
# 在模块内部获取内置变量
# print(__name__)
if __name__ == '__main__':
    print('Berlin模块的测试代码开始执行')
    res1 = my_sum(1,3)
    print(res1)
    res2 = my_sub(3,1)
    print(res2)
    print('Berlin模块的测试代码结束执行')
