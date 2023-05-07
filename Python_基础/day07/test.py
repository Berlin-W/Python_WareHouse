def func(temp):
    a = 10
    print(a)


# 函数调用
func(22)

# NameError: name 'a' is not defined
# print('函数的外部：', a)    # err
# print('函数的外部: ', temp)    # err

# 定义全局变量
num = 10

def func():
    print('func num = ', num)

func()  # 函数调用
print('函数的外面 num = ', num)