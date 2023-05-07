"""
增加	列表.append(值)	在末尾追加数据
删除	列表.remove(值)	删除第一个出现的指定数据
修改	列表[索引] = 值	修改指定索引的数据，数据不存在会报错
查询	列表[索引]	根据索引取值，索引不存在会报错
len(列表)	列表长度(元素个数)
值 in 列表	判断列表中是否包含某个元素，结果是 True 或 False
排序	列表.sort()	升序排序
"""

name_list = ['smart', 'yoyo', 'rock', 'yoyo', 'lily']
# 在前增加数据   在指定位置插入值, 超过索引会追加值   列表.insert(索引, 值) 在指定位置插入值, 超过索引会追加值
# name_list.insert(0,'lucy')
# print(name_list)

# 增加	列表.append(值)	在末尾追加数据
# name_list.append('Berlin')
# print(name_list)
# name_list.append('test_user')
# name_list.append('test_user')
# print(name_list)
# 删除	列表.remove(值)	删除第一个出现的指定数据
# name_list.remove('test_user')
# print(name_list)
# 修改	列表[索引] = 值	修改指定索引的数据，数据不存在会报错
# name_list[3] = 'Tom'
# print(name_list)
# len(列表)	列表长度(元素个数)
# length = len(name_list)
# print(length)
"""
值 in 列表	判断列表中是否包含某个元素，结果是 True 或 False
值 not in 列表 判断列表中是否不包含某个元素，结果是 True 或 False
"""
# print('yoyo' in name_list)
# print('Berlin' not in name_list)

"""
排序	列表.sort()	升序排序  默认是升序
"""

# num_list = [1, 3, 2, 8, 7, 6, 10]
# num_list.sort()
# print(num_list)

#  从大到小排序
# num_list.sort(reverse=True)
# print(num_list)
