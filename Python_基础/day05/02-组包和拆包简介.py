"""
组包：= 右边有多个数据时，会自动包装为元组赋值给 = 左边的变量
"""
# 将 =号邮编的1,2,3包装成一个元祖(1,2,3),然后将元组赋值给=左边变量a
a = 1,2,3
print(type(a),a)


"""
拆包：多个变量 = 容器数据，当变量数量等于容器长度时，容器中的每个元素会按照次序一一赋值给 = 号左边的变量

注意：= 号左边变量的数量必须和 = 号右边容器的长度相等
"""
a,b,c = (1,3,5)
print(a)
print(b)
print(c)

