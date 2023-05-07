"""
列表(list)：python中用来存储一组数据的类型，其中存储的每个数据称为'元素'
定义：列表变量名 = [数据1, 数据2, ...]
访问：列表变量名[位置标号]，列表中元素的位置编号从0开始，位置编号也被称为索引或下标
"""


# 定义一个列表数据：保存 'smart', 'yoyo', 'rock', 'lily' 四个数据
# 编号方式
# 从左到右       0      1      2       3
# 从右到左      -4     -3     -2      -1
# name_list = ['smart','yoyo','rock','lily']
# print(type(name_list),name_list)
#
# # 获取yoyo数据
# print(name_list[1])
# print(name_list[-3])
#


# list1 = [13, 5, 8]
# list2 = [20, 21]

'''插入 insert  在指定位置插入值, 超过索引会追加值'''
# list1.insert(3,9)
# print(list1)

'''列表.extend(可迭代对象) :将可迭代对象 中 的元素 追加到列表'''
# list1.extend(list2)
# print(list1)
# list1.extend(list1)
# print(list1)

'''列表.remove(值) : 删除指定值的 第一个匹配项 '''
# list1.remove(5)
# print(list1)

'''del 列表[索引] 删除指定位置的值 '''
# del list1[1]
# print(list1)

'''列表.pop(索引) 删除指定索引的值, 并返回被删除的值 '''
# res = list1.pop(1)
# print(list1)
# print(res)

'''列表.clear()  清空列表 '''
# list1.clear()
# print(list1)

'''修改索引的值   列表[索引] = 值  修改指定索引的值，索引不存在会报错 '''
# list1[0] = 99
# print(list1)

'''列表[索引]   根据索引取值，索引不存在会报错 '''
# print(list1[2])

'''列表.index(值) 根据值查询索引，返回 第一个匹配项 的索引，没有查到会报错  '''
# index = list1.index(13)
# print(index)

'''len(列表)  列表长度(元素个数)'''
# length = len(list1)
# print(length)

# list3 = [13, 5, 8, 13]
'''列表.count(值) 	值在列表中出现的次数 '''
# count = list3.count(13)
# print(count)

'''
    列表.sort()  升序
    列表.sort(reverse=True)  	降序
 '''
# list3.sort()
# print(list3)
# # list3.sort(reverse=True)
#
# ''' 列表.reverse()  逆序、反转'''
# list1.reverse()
# print(list1)

"""列表.append() 在末尾追加值"""
list1 = [13,5,8]
# 在列表结尾追加8
# list1.append(8)
# print(list1)

"""列表.insert() 在指定位置插入值，超过索引会追加值"""
# list1.insert(1,9)
# print(list1)   # [13,9,5]
# 如果插入值得范围超过索引，就默认在列表末尾追加值
# list1.insert(10,4)
# print(list1) # [13,9,5,4]

"""列表.extend(可迭代对象) 可将可迭代对象中的元素追加到列表"""
# list2 = [20,21]
# 将list2中的元素追加到list1中
# list1.extend(list2)
# print(list1)  # [13, 5, 20, 21]

"""列表.remove() 删除指定值得第一个匹配项"""
# list1 = [13, 5, 8, 5]
# 删除第一个匹配到的5
# list1.remove(5)
# print(list1)  [13, 8, 5]

"""del 列表[索引] 删除指定位置的值"""
# del list1[1]
# print(list1)  [13]

"""列表.pop(索引) 删除指定索引的值，并返回删除的值"""
# res = list1.pop(1)
# print(list1)   # [13, 8]
# print(res) # 5

"""列表.clear() 清空列表"""
# list1.clear()
# print(list1)  # []

"""列表[索引]=值 修改指定索引的值，索引不存在会报错"""
# list1[1] = 9
# print(list1)  # [13, 9, 8]
# 索引不存在,程序报错
# list1[10] = 3

"""列表[索引] 根据索引取值，索引不存在会报错"""
# res = list1[2]
# print(type(res),res)

"""列表.index 根据值查询索引，返回第一个匹配项的索引，没有查到会报错"""
# list1 = [13, 5, 8, 5]
# index = list1.index(5)
# print(index) # 1

"""len(列表) 统计元素的个数"""
# length = len(list1)
# print(length)

"""if 值 in 列表: 判断列表中是否包含某个值"""
# if 5 in list1:
#     print(list1.index(5))
# else:
#     print("不在列表中")

"""列表.count(值) 值在列表中出现的次数"""
# list1 = [13, 5, 8, 13]
# cnt = list1.count(13)
# print(cnt)


"""列表.sort()"""
# 升序排列
# list1.sort()
# print(list1) # [5, 8, 13]
# print("=============")
# 列表降序
# list1.sort(reverse=True)
# print(list1)  # [13, 8, 5]

"""列表.reverse()  逆序、反转 """
list1.reverse()
print(list1)  # [8, 5, 13]