"""
集合：也可以用来存储一组数据，数据唯一，重复元素只保留一个，集合元素不能根据下标取值
定义：
    集合变量 = {数据1, 数据2, 数据3, ...}
"""


# 定义一个集合数据
my_set ={'smart', 'rock', 'yoyo', 'smart'}
print(type(my_set))
# 使用集合对列表数据进行去重
name_list = ['smart', 'rock', 'yoyo', 'smart']
res = set(name_list)
print(res)
# 如何定义一个空集合？
my_set = set()

