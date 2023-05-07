"""
字典(dict)：也可以用来存储多个数据，其中存储的每个数据都包括key(名字)和value(值)，可以通过key取到对应的值
定义：
    字典变量 = {key1: value1, key2: value2, key3: value3}
访问：
    字典变量[key]
"""

# 定义一个字典数据：存储 name 为 'smart', age 为 18, city 为 '上海'
# 字典的键只能是 字符串 元组 数字  值可以是所有
# my_dict = {'name':'smart','age':18,'city':'上海'}
# print(type(my_dict),my_dict)
# #  获取 smart
# print(my_dict['name'])
# # 获取18
# print(my_dict['age'])
# # 获取 上海
# print(my_dict['city'])
#  注意:字典变量[key]取值时,key必须存在,否则出现keyError 错误
"""
增加	字典[键] = 值	键不存在，会添加键值对
修改	字典[键] = 值	键存在，会修改键值对的值
删除	字典.pop(键)	删除指定键值对,返回被删除的值,如果键不存在,会报错
查询	字典[键]	根据键取值，键值对不存在会报错
字典.get(键)	根据键取值，键值对不存在返回None, 不会报错
遍历	
    for key in 字典                  遍历字典，获取所有的键
    for value in 字典.values()       遍历字典，获取所有的值
    for key, value in 字典.items()	遍历字典, 获取所有的键值对 (键, 值)
"""

"""
增加	字典[键] = 值	键不存在，会添加键值对
修改	字典[键] = 值	键存在，会修改键值对的值
"""
# my_dict['address']='浦东新区'
# my_dict['gender']= True
# print(my_dict)
# my_dict['age']= 19
# print(my_dict)
"""
删除	字典.pop(键)	删除指定键值对,返回被删除的值,如果键不存在,会报错
"""
# 返回删除的值
# result = my_dict.pop('gender')
# print(result)


"""
查询	字典[键]	根据键取值，键值对不存在会报错
字典.get(键)	根据键取值，键值对不存在返回None, 不会报错
"""
# print(my_dict.get('name'))
# print(my_dict.get('berlin'))

#  if 键名 in 字典:
# if 'name' in my_dict:
#     print(my_dict['name'])

"""
遍历	
    for key in 字典                  遍历字典，获取字典中所有的键
    for value in 字典.values()       遍历字典，获取字典中所有的值
    for key, value in 字典.items()	遍历字典, 获取字典中所有的键值对 (键, 值)
"""
# for key in my_dict:
#     print(key)  # 遍历键名
#     print(my_dict[key])   # 遍历键值
#     print("================")

# 同时遍历字典的key-value
# for key,value in my_dict.items():
#     print(key,value)
"""添加键值对"""
dict1 = {"name":"张三","age":20}
# 添加键值对
# dict1["age"]=20
# print(dict1)

"""删除键值对 字典.pop() 返回删除的value，键不存在会报错"""
# value = dict1.pop("age")
# print(value)

"""del 字典[键] 键不存在，会报错"""
# del dict1["age"]
# print(dict1)

"""字典.clear() 清空字典中的kv"""
# dict1.clear()
# print(dict1)

"""修改字典[键]=值"""
# dict1["name"]="李四"
# print(dict1)

"""
    字典.update(字典2)
    取出字典2的键值对对字典1操作，键值对不存在，添加键值对；存在则修改值
"""
# dict2 = {"age":22,"height":1.8}
# dict1.update(dict2)
# print(dict1)

"""
    字典.setdefault(键,数据)
    键值对不存在，添加键值对；存在则不做处理
"""
# dict1.setdefault("height",1.8)
# print(dict1)
# 键存在，不做处理
# dict1.setdefault("age",22)
# print(dict1)

"""根据键取值"""
# list1=[13,5]
# dict2 = {"name":"张三"}
# print(dict2["name"])
# 键不存在，会报错
# print(dict2["height"])

"""字典.get(键) 根据键取值，键值对不存在返回None, 不会报错"""
# print(dict1.get("name"))
# print(dict1.get("height"))

"""
    遍历字典中所有的key
    for key in 字典:
"""
# for key in dict1:
#     print(key)

"""for key in 字典.keys()"""
# for key in dict1.keys():
#     print(key)

""" 
    遍历字典中所有的value
    for value in 字典.values():
"""
# for value in dict1.values():
#     print(value)

"""
    遍历字典所有的键值对
    for key,value in 字典.items():
        print(key,value)
"""
# for key,value in dict1.items():
#     print(key,value)
