"""
使用模块时起别名
学习目标：能够在使用模块时通过as关键字起别名，解决名称冲突的问题
"""
# 场景
# ① 模块名称或模块中的内容名称过长
# ② 模块名称或者模块中的内容跟当前文件中的名称有冲突
"""

情况1：给模块起别名
    import 模块名 as 别名
    
情况2：给模块中导入的内容起别名
    from 模块名 as 别名

注意：一旦起了别名之后，那么只能通过别名使用相应的内容
"""
# 情况1: 给模块起别名
#  import 模块名 as 别名
from Berlin import my_sum as berlin_sum,my_sub as berlin_sub
res1 = berlin_sum(1,2)
res2 = berlin_sub(5,3)
print(res1)
print(res2)




