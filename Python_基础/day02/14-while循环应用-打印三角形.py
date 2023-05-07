"""
需求：打印效果如下
*
* *
* * *
* * * *
* * * * *
"""
i = 1
while i <= 5:
    j = 0
    while j < i:
        print("* ",end="")
        j += 1
    print()
    i += 1

"""
     需求打印： 倒三角
"""
print("===================================")
i = 1
while i <= 5:
    j = 5
    while j >= i:
        print("* ",end="")
        j -= 1
    print()
    i += 1


