"""
函数的嵌套调用：在一个函数的代码中调用了另外一函数
"""


def func01():
    print('开始调用func01')
    print('结束调用func01')


def func02():
    print('开始调用func02')
    print('结束调用func02')


func02()

"""
需求：
1）设计一个函数，打印一行分隔线：可指定数量，可指定分隔线字符的样式 
    如： 一行分隔线字符的数量为5，字符样式为'$ ' 
    $ $ $ $ $
    
2）设计一个函数，打印n行分隔线，可指定一行分隔线字符的数量，可指定分隔线字符的样式 
    如：3行分隔线，一行分隔线字符的数量为5，字符样式为'$ '
    $ $ $ $ $
    $ $ $ $ $
    $ $ $ $ $
"""
# 一行分隔线字符的数量为5，字符样式为为$
# 分析: 字符数量为5: 函数第一个输入为数字,
#      字符样式为 '$',函数第二个输入为字符串


def print_line(num,char):
    """
    :param num:
    :param char:
    :return:
    """
    print(num * char)



#  如：3行分隔线，一行分隔线字符的数量为5，字符样式为'$
# 分析: 3行分隔线  函数需要一个表示行数的实参
# 一行分隔线字符的数量为5 函数需要一个表示字符数量的实参
# 字符样式为'$ ,函数需要一个表示字符的实参
#  设计: 需要用到函数调用.输出3行分隔线,需要利用循环,调用三次 print_line(num,char)函数,完成打印输出
def print_lines(n,num,char):
    """
    :param n:  表示函数调用的次数
    :param num: 表示被调用函数输出的个数
    :param char: 表示被调用函数输出的样式
    :return:
    """
    i = 0
    while i < n:
        print_line(num,char)
        i += 1

print_lines(6,6,'$')
print("*"*10)
"""
需求：
1）设计一个函数求三个数的和

"""
def sum(num1,num2,num3):
    res =f"三个数的和为:{num1+num2+num3}"
    return res

# res = sum(1,2,3)
# print(res)

# 2）设计一个函数求三个数的平均值
def avg(num1,num2,num3):
    # res = f"三个数的平均值为:{(num1+num2+num3)/3.}"
    res = (num1+num2+num3)/3
    return res

print(avg(1,2,3))
