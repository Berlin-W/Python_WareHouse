# 综合1
#        012345678
#

'''
综合 2
'''
# #       0123456789
# str1 = '1234567890'
# # 截取字符串的第一位到第三位的字符
# print(str1[0:3])
# # 取字符串最后三位的字符
# print(str1[7:])
# # 截取字符串的全部字符
# print(str1[::])
# # 截取字符串的第七个字符到结尾
# print(str1[6:])
# # 截取字符串的第一位到倒数第三位之间的字符
# print(str1[0:8])
# #  截取字符串的第三个字符
# print(str1[2:3])
# # 截取字符串的倒数第一个字符
# print(str1[-1:-2:-1])
# # 截取与原字符串顺序相反的字符串
# print((str1[-1::-1]))
# # 截取字符串倒数第三位与倒数第一位之间的字符
# print(str1[7:])
# # 截取字符串的第一位字符到最后一位字符之间的字符，每隔一个字符截取一次。
# print(str1[0::2])

'''综合3
    将下列两个列表合并，将合并后的列表去重，之后降序并输出
    list1 = [11, 45, 34, 51, 90]  list2 = [4, 16, 23, 0]
'''
# list1 = [11, 45, 34, 51, 90]
# list2 = [4, 16, 23, 0]
# list3 = list1 + list2
# # 倒叙
# list4 = set(list3)
# list5 = list(list4)
# list5.sort(reverse=True)  # 排序后仍是列表
# print(list5)


'''
    综合4 
    现有：`typle1 = ("tom","kaisa","alisi","xiaoming","songshu")`
     我想获得“alisi”这个内容
'''
# typle1 = ("tom","kaisa","alisi","xiaoming","songshu")
# print(typle1[2])
#
# # 分割
# list1 = list(typle1)
# print(list1[2])

'''
定义一个函数max，接受的参数类型是数值，最终返回两个数中的最大值
'''
# def max(num1,num2):
#     if num1 > num2:
#         temp = num1
#     else:
#         temp =num2
#
#     return temp
#
# num1 = int(input('请输入数字:'))
# num2 = int(input('请输入数字:'))
# _max = max(num1,num2)
# print(_max)
'''
    用函数实现一个判断用户输入的年份是否是闰年的程序，在函数中打印结果。
'''
# def is_runYear(year):
#     if year % 400 == 0 or (year % 4 == 0  and year % 100 != 0):
#         print(f'{year}是闰年!')
#     else:
#         print(f'{year}不是闰年!')
#
#
# year = int(input('请输入年份:'))
# is_runYear(year)

'''
定义一个函数，计算两个数之和。调用者在得到结果的时候需要判断是否大于20，如果大于则输出，超过10的加法太难了
'''
# def my_add(num1,num2):
#     _sum = num1 + num2
#     if _sum > 20:
#         print(f'两数的和是:{_sum},超过10的加法太难了')
#     else:
#         print('加法 so easy!')
#
#
# num1 = int(input('请输入数字:'))
# num2 = int(input('请输入数字:'))
# my_add(num1,num2)

'''
    综合8 : 完成一个函数，给定三个值。判断你给的值是否可以组成一个三角形
'''
# def is_trangle(a,b,c):
#     if a + b > c and a + c > b and b + c > a:
#         print(f'由 {a},{b},{c}三条边组成的图形满足三角形的定义')
#     else:
#         print(f'由 {a},{b},{c}三条边组成的图形不满足三角形的定义')
#
#
# a = int(input('请输入第一条边:'))
# b = int(input('请输入第二条边:'))
# c = int(input('请输入第三条边:'))
# is_trangle(a,b,c)

'''
    扩展提1:定义一个函数，接受三个参数，分别为字符串s、数值a1、数值a2，
    将字符串s从下标a1开始的a2个字符删除，并把结果返回，a2默认值为0
'''
# def res(str,num1,num2):
#     str1 = str[:num1] + str[num2 + 1: ]
#     print(str1)
# #      012345678
# str = '123456789'
# res(str,3,6)
'''
    扩展题2 
'''
def recieve(num,command = False):
    list1 = []
    i = 0
    while i <= num:
        if command :
            if i % 2 == 0:
                list1.append(i)
                print(list1)
        else:
            if i % 2 != 0:
                list1.append(i)
                print(list1)

        i += 1

    print(f'最后的结果为:{list1}')
    # return list1
recieve(10,True)
