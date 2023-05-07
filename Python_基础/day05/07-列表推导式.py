"""
列表推导式：快速生成列表元素的表达形式，通过for添加列表元素的简洁写法
推导式基本格式： [计算公式 for 循环 if 判断]
特点：
    1）每循环一次，将计算公式的结果添加到列表中
    2）计算公式可以使用遍历出的数据
    3）for 遍历出的数据 必须满足 if 判断 才会使用计算公式生成元素
"""

"""
需求：产生列表[0, 1, 2, 3, 4]
"""
new_list1=[]
for i in range(0,5):
    new_list1.append(i)
print(new_list1)

new_list2=[i+1 for i in range(0,5)]
print(new_list2)

# 列表推导式:基本格式[计算公式 for 循环]
#
my_list = [i for i in range(0,5)]
print(my_list)




"""
需求：产生列表[0, 2, 4, 6, 8, 10]
"""
my_list1 = [i for i in range(0,11,2)]
print(my_list1)


"""
需求：有一个字符串'hello'，生成['h', 'e', 'l', 'l', 'o']
"""
_str = 'hello'
my_list2 = [c for c in _str[0:]]
print(my_list2)

# 推导式基本格式： [计算公式 for 循环 if 判断]
#  每执行一次for循环,先去判断后面的条件,条件成立时,才计算
my_list3 = [ i for i in range(0,11) if i % 2 == 0]
print(my_list3)