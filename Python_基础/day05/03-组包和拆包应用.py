"""
应用1：交换 a，b 两个变量的值
"""

a = 10
b = 20
a,b = b,a
# 先将=右边变量b和a的值组包成元组:(20,10)
# 然后再讲元组(20,10) 拆包成数字20,10,分别赋值给a,b
print(a,b)


"""
应用2：函数同时返回多个结果
"""
def func1():
    # 返回三个结果
    # 组包:当函数返回多个结果时,会将多个结果先组包成一个元组,再返回
    return 1,3,6


# <class 'tuple'> (1, 3, 6)
# result = func1()
# print(type(result),result)



"""
应用3：字典元素拆包
"""

user_dict = {'name': 'smart', 'age': 18}
# for key,value in user_dict.items():
#     print(key,value)


for item in user_dict.items():
    key,value=item
    print('key:',key)
    print('value:',value)
