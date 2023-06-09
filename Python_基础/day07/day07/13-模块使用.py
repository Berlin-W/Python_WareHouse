"""
模块的使用
学习目标：知道如何使用模块中的变量、函数、类等
"""

"""
方式1【推荐】：导入整个模块，然后通过`模块名.要使用的内容`进行使用
    import 模块名

方式2【推荐】：从模块中导入指定要使用的内容，然后进行使用【推荐】
    from 模块名 import 要使用的内容

方式3【不推荐】：导入模块中的所有内容，然后进行使用
    from 模块名 import *
"""
# 方式1：导入整个模块，然后通过`模块名.要使用的内容`进行使用
#     import 模块名
import smart

print(smart.num)

res = smart.my_sum(1, 3)
print(res)

res = smart.my_sub(3, 1)
print(res)


# 方式2【推荐】：从模块中导入指定要使用的内容，然后进行使用【推荐】
#     from 模块名 import 要使用的内容
from smart import num, my_sum, my_sub

print(num)

res = my_sum(1, 3)
print(res)

res = my_sub(3, 1)
print(res)


# 方式3【不推荐】：导入模块中的所有内容，然后进行使用
#     from 模块名 import *
from smart import *

print(num)

res = my_sum(1, 3)
print(res)

res = my_sub(3, 1)
print(res)