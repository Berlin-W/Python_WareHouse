"""
enumerate：通过 for 配合 enumerate 遍历容器同时获取元素索引位置(下标)、元素
 # 变量1 是容器中数据的下标
 # 变量2 是容器中的每个数据
"""

user_list = [{'name': 'mike', 'age': 34, 'tel': '110'},
             {'name': 'yoyo', 'age': 18, 'tel': '120'}]

"""
需求：遍历 user_list 数据时，同时打印出每个元素及元素的下标
"""
# 变量i为数据的下标  user为数据对象
# for i,user in enumerate(user_list):
#     print(i,user)
#     print(type(user))


for user in enumerate(user_list):
    print(user)
    # enumerate 遍历容器返回的是元组
    print(type(user))
'''
(0, {'name': 'mike', 'age': 34, 'tel': '110'})
<class 'tuple'>
(1, {'name': 'yoyo', 'age': 18, 'tel': '120'})
<class 'tuple'> 是一个 组包
'''
# 1. 定义索引位置变量
i = 0
# 2. for遍历列表，打印：索引、元素
for user_dict in user_list:
    print(i, user_dict)
    # 3. 索引位置+1
    i += 1


print("* "*20)
for i,user in enumerate(user_list):
    print(i,user,type(user))

"""
del：通过del根据下标删除列表元素
格式：del 列表[索引]
"""
print("* "*20)
user_list = [{'name': 'mike', 'age': 34, 'tel': '110'},
             {'name': 'yoyo', 'age': 18, 'tel': '120'}]

del user_list[1]
print(user_list)

