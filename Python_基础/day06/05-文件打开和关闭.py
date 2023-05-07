"""
程序操作文件流程：
    打开文件，或者新建立一个文件 => 读写数据 => 关闭文件(释放资源)
"""

"""
python中文件操作相关函数

1）文件变量 = open(文件名字，访问模式)
    打开一个已经存在的文件，或者创建一个新文件
2）文件变量.close()
    关闭文件，为了释放操作文件占用的系统资源
"""
# 打开一个已经存在的文件，或者创建一个新文件 文件已存在，会先清空
file = open('xxx.txt','r')

# 打开文件
# w写模式打开文件时，
# 1）如果文件不存在，会自动创建
# 2）如果文件已存在，打开之后内容会先清空
f = open('abc.abc.txt', 'w') # write：写


# r读模式打开文件时，文件必须存在，否则会出现错误
# FileNotFoundError: [Errno 2] No such file or directory: 'abc.abc.txt'
f = open('abc.abc.txt', 'r') # read：读


# 关闭文件目的：释放文件操作时占用系统资源(内存)
# f.close()

"""
自动关闭文件：使用 with 关键字

with open(文件名字，访问模式) as 文件变量:
    # 操作代码...
    # 操作代码...
    # 操作代码...
    
注意：当 with 语句块下面的代码执行完成之后，会自动关闭文件
"""

# f = open('abc.abc.txt', 'r')
with open('abc.abc.txt', 'r') as f:
    print('文件操作')
    print('文件操作')
    print('文件操作')
    print('文件操作')


# 05-文件打开和关闭在day06目录下，这里的.表示当前目录，就是day06目录
# with open('./code2/test2.txt', 'r') as f:
#     res = f.read()
#     print(res)

