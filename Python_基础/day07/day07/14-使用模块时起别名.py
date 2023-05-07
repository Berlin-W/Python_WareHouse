"""
使用模块时起别名
学习目标：能够在使用模块时通过as关键字起别名，解决名称冲突的问题
"""

# 场景：
# ① 模块名称或模块中的内容名称过长，想变短一点
# ② 模块名称或模块中的内容名称跟当前文件中的名称有冲突

"""
情况1：给模块起别名
    import 模块名 as 别名
    
情况2：给模块中导入的内容起别名
    from 模块名 import 内容 as 别名

注意：一旦起了别名之后，那么只能通过别名使用相应的内容
"""

# 情况1：给模块起别名
#     import 模块名 as 别名
# import smart as sm
#
# print(sm.num)
#
# res = sm.my_sum(1, 3)
# print(res)

# 情况2：给模块中导入的内容起别名
#     from 模块名 import 内容 as 别名
from smart import my_sum as sm_sum, my_sub as sm_sub


def my_sum(a, b):
    """计算两个数的和，并打印到屏幕上"""
    res = a + b
    print('res=', res)


res = sm_sum(1, 3)
print(res)

