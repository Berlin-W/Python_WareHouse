a = [11,22,33]
print(a[1])
# 删除 22
a.remove(22)
print(a)
# 向列表中添加（增）新元素 44
a.append(44)
print(a)
# 修改（改）列表中的元素 22 为 55
a[1]=55
print(a)
# 查找（查）列表中的元素 55 的下标
index =  a.index(55)
print(index)