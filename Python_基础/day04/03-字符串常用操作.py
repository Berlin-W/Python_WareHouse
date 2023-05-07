"""
查找	字符串.find(目标字符串, 开始索引, 结束索引)	在指定范围内, 查询目标字符串的索引, 不存在返回-1
替换	字符串.replace(原内容, 新内容, 替换次数)	返回一个替换了原内容的新字符串，可以指定替换次数
分割	字符串.split(分割符)	以分割符拆分字符串, 返回列表
拼接	字符串 + 字符串	拼接两个字符串
字符串.join(字符串列表)	以字符串来连接字符串列表中每个元素，合并为一个新的字符串
"""

"""
查找	字符串.find(目标字符串, 开始索引, 结束索引)	在指定范围内, 查询目标字符串的索引, 不存在返回-1
"""
my_str = 'hello python! life is short, you need python!'

# 需求：从 my_str 字符串中查找 python  查找的是第一个出现的值的下标
# index_1 = my_str.find('python')
# print(index_1)
# rfind()方法从右边开始找,返回字符串出现的位置
# index_2 = my_str.rfind('python')
# print(type(index_2),index_2)


# 需求：从 my_str 字符串中查找 itheima
# res = my_str.find('itheima')
# print(res)

"""
字符串.index(目标字符串, 开始索引, 结束索引)
在指定范围内, 查询目标字符串的索引, 不存在会报错
"""
result = my_str.index('life')
print(result)
"""
替换	字符串.replace(原内容, 新内容, 替换次数)	返回一个替换了原内容的新字符串，可以指定替换次数
"""

# 需求：将 my_str 字符串中的 python 替换为 itheima
# new_str = my_str.replace('python','itheima',1)   #  返回一个新的字符串  原来的字符串没发生改变
# print(new_str)
# print(my_str)



"""
分割	字符串.split(分割符)	以分割符拆分字符串, 返回列表
"""

# 需求：将 my_str 字符串按照空格分隔成列表数据
res = my_str.split(',')
print(type(res),res)

"""
拼接	字符串 + 字符串	拼接两个字符串
字符串.join(字符串列表)	以字符串来连接字符串列表中每个元素，合并为一个新的字符串
"""
# str1 = 'hello '
# str2 = 'python'

# 需求：将 str1 和 str2 拼接成 'hello python'
# print(str1 + str2)

# 需求：将 str_list 使用空格连接成一个字符串
# str_list = ['hello', 'python!', 'life', 'is', 'short,', 'you', 'need', 'python!']
# res = ' '.join(str_list)
# print(res)

"""
字符串.strip(目标字符串)
返回新字符串，去除 字符串 左右两边的目标字符串, 不设置目标字符串则去除空格
"""
str1 = "--hello---"

# 去除两端目标字符串
str2 = str1.strip("-")
print(str2)  # hello
