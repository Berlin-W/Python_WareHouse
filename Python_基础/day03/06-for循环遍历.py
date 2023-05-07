"""
遍历：从前到后依次取出列表中的每个元素
"""


# 需求：遍历打印name_list中的每个元素

"""
while循环实现
"""
# 从右到左
# name_list = ['smart', 'yoyo', 'rock', 'lily']
# i = -1
# while i >= -4:
#     print(name_list[i])
#     i -= 1
# print('----------')
# # 从左到右
# i = 0
# while i < len(name_list):
#     print(name_list[i])
#     i += 1
"""
for循环实现：依次从列表中取出每个元素，赋值给前面的变量
语法：
    for 变量 in 列表(可迭代数据):
        ...
"""

# 列表元素的遍历
name_list = ['smart', 'yoyo', 'rock', 'lily']
# for i in name_list:
#     print(i)

"""
for循环中的else: 和while的else一样，当循环中没有遇到break，循环结束时会执行else部分的代码
"""

for name in name_list:
    print(name)
else:
    print('当循环中没有遇到break，循环结束时会执行else部分的代码')

# print('for循环结束')
