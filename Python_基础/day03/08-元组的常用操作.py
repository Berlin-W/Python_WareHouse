"""
元组[索引]	根据索引取值，索引不存在会报错
len(元组)	元组长度(元素个数)
值 in 元组	判断元组中是否包含某个值
"""

tuple1 = (13, 5, 8)
"""元组[索引] 根据索引取值，索引不存在会报错"""
# 获取索引1 对应的值
# print(tuple1[1])  # 5
# print(tuple1[10])  # 报错

"""元组.index(值) 根据值查询索引，返回 第一个匹配项 的索引，没有查到会报错"""
# tuple1 = (13, 5, 8, 5)
# index = tuple1.index(5)
# print(index)

"""len(元组) 元素个数"""
# length = len(tuple1)
# print(length)


"""if 值 in 元组:"""
# 判断元组中是否包含数据5
# if 5 in tuple1:  # 包含数据,返回True; 不包含,返回False
#     print("元组中包含该数据")
# else:
#     print("元组中不包含该数据")

"""元组.count(值) 值在元组中出现的次数"""
# tuple1 = (13, 5, 8, 13)
# # 获取元组中 13 出现的次数
# count = tuple1.count(13)
# print(count)  # 2

