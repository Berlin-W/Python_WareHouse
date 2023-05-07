"""
制作py模块
学习目标：能够自己制作一个py模块
"""

"""
注意：
1）制作的 python 模块不能是数字开头

重要的事情说3遍：
    smart.py 就是制作的模块！！！
    smart.py 就是制作的模块！！！
    smart.py 就是制作的模块！！！
"""
# 方式一 :导入整个模块,然后通过模块名,要使用的内容进行使用
# import Berlin
# sum = Berlin.my_sum(1,2)
# print(sum)
# print(Berlin.num)

# 方式二 :  from 模块名 import + 导入的内容,然后进行使用
from Berlin import num,my_sub,my_sum
print(num)
res1 = my_sub(5,3)
print(res1)
res2 = my_sum(6,3)
print(res2)
