# 定义一个内置变量：__all__，来限定 from 模块名 import * 时导入哪些内容
__all__ = ['num', 'my_sum', 'my_sub']


# 定义一个变量
num = 10


# 定义一个函数：my_sum，计算两个数字的和
def my_sum(a, b):
    """计算两个数字的和"""
    return a + b


# 定义一个函数：my_sub，计算两个数字的差
def my_sub(a, b):
    """计算两个数字的差"""
    return a - b


# 在 smart 模块内部获取内置变量：__name__
# print(__name__) # '__main__'

if __name__ == '__main__':
    # 在模块内部添加一些测试代码，测试模块中的功能是否功能
    print('smart模块的测试代码开始执行')
    # 测试 my_sum
    res = my_sum(1, 3)
    print(res)
    # 测试 my_sub
    res = my_sub(3, 1)
    print(res)
    print('smart模块的测试代码结束执行')
