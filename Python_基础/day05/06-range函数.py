"""
range函数：产生一段指定范围内的列表数字，一般配合for循环进行使用

使用：range(起始数字, 结束数字, 步长)

注意：产生的列表数据中，包含起始数字，不包含结束数字
"""
# 需求:生成1-10之间的数字
# result = range(1,11,1)
# print(list(result))
# _sum = 0
# for i in range(1,11):
#     _sum += i
#
#
# print(_sum)


"""
示例：for循环计算1-100的数字和
"""
_sum = 0
for i in range(1,101):
    _sum += i

print(_sum)


"""
示例：for循环计算1-100的偶数和
"""
_sum = 0
for i in range(2,101,2):
    _sum += i

print(_sum)




