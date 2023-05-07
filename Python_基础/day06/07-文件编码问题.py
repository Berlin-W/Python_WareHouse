"""
文件编码问题
"""
# 中 -> 10000
# 中 -> 20000

"""
文件里面的内容不管是什么内容，其实存储在硬盘上 都是以数字的形式存放

所谓编码，其实就是文件中的每个内容在硬盘上存储时，用什么位数字表示的一种规定

文件编码问题主要是针对文件中存储的中文内容，在存储中文时，计算机有很多种不同的
编码方式，所谓的编码就是如何在计算机中表示这个中文文字，常见的编码方式有：gbk，utf8。

比如中文文字"花"：
    "花"的utf8编码为：&#x82B1;
    "花"的gbk编码为：\u82b1

当我们通过程序读取文件内容时，如果文件本身是utf8编码，而我们用gbk编码解析，
或者如果文件本身是gbk编码，而我们用utf8编码解析，那么文件操作就会出现乱码或错误。

注意：
1）windows操作系统下，open操作文件时，encoding参数默认为gbk
2）linux/mac操作系统下，open操作文件时，encoding参数默认为utf8

3）pycharm双击打开文件时，无论什么操作系统，都是使用utf8方式加载

使用：
    文件变量 = open('操作文件', '访问模式', encoding='编码方式')
"""

# 以后进行文件操作时，推荐使用utf8的编码方式
# with open('C:/Users/魏博林/Desktop/test.txt','r',encoding='UTF8') as  file:
#      content = file.read()
#      print(content)


# 以UTF8编码方式写入一个文件
# with open('utf8-file.txt','w',encoding='utf8') as file1:
#     file1.write('这是一个以utf8编码的文本文件')
#
# 以GBK编码方式写入一个文件
# with open('gbk-file.txt', 'w', encoding='gbk') as file2:
#     file2.write('这是一个gbk编码的文本文件')

# 以UTF8编码方式读取一个文件
# with open('utf8-file.txt', 'r', encoding='utf8') as f:
#     res = f.read()
#     print(res)

# 以GBK编码方式读取一个文件
# with open('gbk-file.txt', 'r', encoding='gbk') as f:
#     res = f.read()
#     print(res)

