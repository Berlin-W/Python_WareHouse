"""
可变类型：在存储空间中可以直接修改的数据类型
    列表、字典、集合
不可变类型：在存储空间中不能修改的数据类型
    数值(int/float/bool)、字符串、元组


【可变类型与不可变类型的本质】：
    在内存地址不变的情况下，能否改变其中的数据，若能则是可变类型，若不能则是不可变类型
"""


# 可变类型：演示列表 集合
my_list = ['a', 'b']

print('修改之前：', id(my_list), my_list)
my_list.append('c')
print('修改之后：', id(my_list), my_list)

print('=' * 20)

# 【可变类型与不可变类型的本质】：
#     在内存地址不变的情况下，能否改变其中的数据，若能则是可变类型，若不能则是不可变类型
# 不可变类型：演示int  元组
a = (10,20)
print('修改之前：', id(a))
a = (10,20,30)
print('修改之后：', id(a))

 
