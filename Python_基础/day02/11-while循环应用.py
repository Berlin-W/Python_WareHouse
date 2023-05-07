"""
while循环应用
"""
"""
需求：计算1~100的累加和（包含1和100）
"""
i,_sum1= 1,0
while i <= 100:
    _sum1 += i
    i += 1
print(_sum1)


"""
需求：计算1~100之间偶数的累加和-方式1
 """
# i = 1
# _sum2 = 0
# while i <= 100:
#     if i % 2 == 0:
#         _sum2 += i
#     i += 1
# print(_sum2)
i = 1
_sum1 = 0
while i <= 100:
    if i % 2 == 0:
        _sum1 = _sum1 + i
    i += 1
print(_sum1)



"""
需求：计算1~100之间偶数的累加和-方式2
"""
i = 2
_sum3 = 0
while i <= 100:
    _sum3 += i
    i += 2
print(_sum3)

















