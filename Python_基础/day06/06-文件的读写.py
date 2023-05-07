"""
文件的读写：通过文件变量可以进行文件的读写操作
"""

"""
文件对象相关函数：
1）write：向文件中写入数据
    使用方式 => 文件变量.write(要写入的内容)
    
2）read：从文件中读取数据
    使用方式 => 文件变量.read(读取的字符数量)
    注意：如读取的字符数量不设置，则默认全部读取
    
3）readline：每次读取文件中的一行数据
    使用方式 => 文件变量.readline()

4）readlines：一次读取文件中的所有行数据
    使用方式 => 文件变量.readlines()
    注意：readlines函数返回的是列表，列表中的每个元素是每一行数据
"""
with open('xxx.txt','w') as file:
    # file.write('hello world \n')
    # file.write('hello python')
    '''
        TypeError: write() argument must be str, not int
        write() 只能向文件中写入字符串 
        file.write(100)  错误
    '''

"""
write：向文件中写入数据
"""
# 打开文件
# io.UnsupportedOperation: not writable
# f = open('abc.abc.txt', 'r')
# f = open('abc.abc.txt', 'w')
#
# # 向文件中写数据
# f.write('hello python')
# f.write('hello itcast')
#
# # 文件关闭
# f.close()
#
# with open('abc.abc.txt', 'w') as f:
#     # 向文件中写数据
#     f.write('hello python')
#     f.write('hello itcast')

"""
read：从文件中读取数据  read()  读取全部内容
"""
# with open('abc.abc.txt', 'r') as f:
#     # 首先从文件中读取4个字符
#     res = f.read(4)
#     print(res)
#     # 再从文件中读取4个字符
#     res = f.read(4)
#     print(res)
#     # 基于上次文件读取的位置，向后读取出所有的内容
#     res = f.read()
#     print(res)

"""
readline：每次读取文件中的一行数据
"""

with open('abc.abc.txt', 'r') as f:
    # 从文件中读取一行数据
    res = f.readline(20)
    print(res)
    # # 再从文件中读取一行数据
    # res = f.readline()
    # print(res)
    # # 再从文件中读取一行数据
    # res = f.readline()
    # print(res)
    # # 再从文件中读取一行数据
    # res = f.readline() # 当文件已经读取到默认时，再次读取内容时，得到的结果是：''
    # print(res)


"""
readlines：一次读取文件中的所有行数据
"""
# with open('abc.abc.txt', 'r') as f:
#     res = f.readlines() # 读取文件中的所有行，返回值是一个list，列表中的每一个数据是文件的每一行内容
#     print(type(res), res)


