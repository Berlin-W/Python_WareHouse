"""
绝对路径：是指文件在硬盘上真正存在的路径，是电脑完整的路径  (从磁盘根目录开始)
相对路径：目标文件相对于当前位置所处的位置（基于一个文件的位置去找另一个文件位置
"""

"""
绝对路径：
1）'C:\\Users\\smart\\Desktop\\pycode\day06\\code1\\test1.txt'
    注意：在 python 程序中，\具有特殊作用，\和紧跟其后的第一个字符结合往往具有特殊意义，
    并不表示\本身，要想表示斜杆本身，必须用 \\ 表示，但更推荐在打开文件时，文件路径中的 \ 换为 /
    
    如：
    a）'C:\\Users\\smart\\Desktop\\pycode\\day06\\code1\\test1.txt'
    b）'C:/Users/smart/Desktop/pycode/day06/code1/test1.txt' (推荐写法)

相对路径：基于一个文件的位置去描述另一个文件位置
    假如现在有 2 个路径：
    1）路径1：'C:/Users/smart/Desktop/pycode/day06/code1/test1.txt'
    2）路径2：'C:/Users/smart/Desktop/pycode/day06/code1/test2.txt'
    
.：当前目录
..：上一级目录

假如我现在处于 code1 目录下：
    问题1：那么如何基于我现在所处的位置描述 test1.txt 文件所在的位置？
    答：我们可以这样描述，在我当前所处的目录下，有一个 test1.txt 文件，在程序中，.表示当前目录，所以
    test1.txt文件的路径可以表示为：./test1.txt，其实.可以省略：test1.txt
    
    问题2：那么如何基于我现在所处的位置描述 test2.txt 文件所在的位置？
    答：我们可以这样描述，在我所处目录的上级目录下，有一个 code2 目录，code2 目录下有 test2.txt
    文件，在程序中，..表示上级目录，所以test2.txt文件的路径可以表示为：../code2/test2.txt
"""


# 绝对路径访问 test1.txt 和　test2.txt
# test1.txt绝对路径：C:\Users\smart\Desktop\pycode\day06\code1\test1.txt
# test2.txt绝对路径：C:\Users\smart\Desktop\pycode\day06\code2\test2.txt

# \：反斜杠
# /：正斜杆
# with open('C:\\Users\\smart\\Desktop\\pycode\\day06\\code1\\test1.txt', 'r') as f:
#     res = f.read()
#     print(res)

# 推荐使用第二种
f = open('C:/Users/魏博林/Desktop/test.txt','r')
res = f.read(4)
print(res)
res = f.read()
print(res)
res = f.readline()
print(res)
f.close()




# 相对路径访问 test1.txt 和 test2.txt
# .：当前目录
# ..：上一级目录
# 基于 09-绝对路径和相对路径.py 文件所处的位置描述
# test1.txt 和 test2.txt 文件的位置
# test1.txt相对路径：./test1.txt
# test2.txt相对路径：../code2/test2.txt

# with open('./test1.txt', 'r') as f:
#     res = f.read()
#     print(res)
#
#
# with open('../code2/test2.txt', 'r') as f:
#     res = f.read()
#     print(res)

# f = open('C:\\Users\\魏博林\\Desktop\\test.txt','r')
# res =f.read()
# print(res)
# m = open('C:/Users/魏博林/Desktop/test.txt','r')

















