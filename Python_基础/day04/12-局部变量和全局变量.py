"""
局部变量：
1）函数的形参以及函数内部定义的变量，作用域只在函数内部(只在函数内部有效)
2）不同函数的局部变量可以同名，互不影响
3）局部变量的作用是存储需要临时存储的数据
"""


def func1(num):
    my_str = 'hello'
    print(num)
    print(my_str)


def func2(num):
    print(num)


func1(10)

# NameError: name 'num' is not defined
# print(num)

# NameError: name 'my_str' is not defined
# print(my_str)

# 定义全局变量
num = 10


def func():
    # 函数内给一个变量赋值时，重新生成一个局部变量num
    # 函数内的num和外面的num没有关系
    global num
    num = 250
    print('func num = ', num)  # 获取是函数内的num


func()  # 函数调用

# 函数外获取的是全局变量的值
print('函数的外面 num = ', num)
"""
全局变量：
1）在函数外部定义的变量
2）全局变量能够在所有的函数中进行访问(不修改)
"""

print("* " * 20)


# 元组不定长形参,传入之后包装成元组类型,用于接收任意数量的位置形参
def func1(*args):
    print(type(args), args)


func1(1, 2, 3)
print("* " * 20)


#  字典不定长形参,传入之后包装成字典类型,且字典可变形必须放到最右侧
def fun2(name, age, **kwargs):
    print('姓名:', name)
    print('年龄:', age)
    print('字典类型:', kwargs)
    print(kwargs)

print("* " * 20)
fun2(name="zcx",age='28',is_married="yes",city="河南省驻马店",phone_number="139xxxx")