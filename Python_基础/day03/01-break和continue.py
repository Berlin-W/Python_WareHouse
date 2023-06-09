"""
break：跳出循环，结束循环代码的执行
continue：本次循环 continue 之后的代码不再执行，直接重新执行循环代码
"""

"""
break案例：
    需求：跑步10圈，跑5圈后，不再跑了
"""

i = 0
while i < 10:
    print('跑步%d圈' % (i+1))
    if i == 4:
    # i向上增加1
        print('休息一下')
        break
    i += 1





"""
continue案例：
    需求：跑步10圈，到第5圈休息一下，第6圈继续
"""

# i = 0
# while i < 10:
#     if i == 4:
#         print('休息一下')
#         # i向上增加1
#         """
#         i += 1 的目的是避免死循环,因为 如果不加1,当i=4时,执行continue 直接跳过后面的代码,此时i还是=4,一直循环
#         当 i += 1时, 跳过循环,执行下一次循环时,i=5,继续执行
#         """
#         i += 1
#         continue
#     print('跑步%d圈' % (i + 1))
#     i += 1



