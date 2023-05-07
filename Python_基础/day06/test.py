'''综合一 '''
# file1 = open('test01.txt','w',encoding='utf8')
# while True:
#     _str = input('请输入一个字符：')
#     if _str == '#':
#         break
#     file1.write(_str)
#
# file1.close()
#
# file2 = open('test01.txt','r',encoding='utf8')
# content = file2.read()
# print(content)
# file2.close()

''' 综合二 '''
# _str = input('请输入一串字符串：')
# A_str =  _str.upper();
# with open('test.txt','w',encoding='utf8') as file:
#     file.write(A_str)
#
# file2 = open('test.txt','r',encoding='utf8')
# content = file2.read()
# print(content)
# file2.close()

'''
综合三
从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件”test”中保存。 
'''
# file = open('test02_3.txt','w',encoding='utf8')
# content = 'python是我用过的最好用，最优雅的计算机语言，没有之一！！！'
# file.write(content)
# file.close()

file2 = open('test02.txt','r',encoding='utf8')
content = file2.read()
print(content)
my_list = content.split('，')
num = content.count('，')
print(num)

#
# with open('test02_1.txt','w',encoding='utf8') as file1:
#     file1.write(my_list[0])
#
# with open('test02_2.txt','w',encoding='utf8') as file2:
#     file2.write(my_list[1])
#
# with open('test02_3.txt','w',encoding='utf8') as file3:
#     file3.write(my_list[2])

'''
    综合4  
    在python用户目录下创建python基础班文件夹
'''
# import os
#
#
# os.mkdir('python基础班文件夹')
# file = open('python基础班文件夹/gai_lun.txt','w',encoding='utf8')
# file.write('德玛西亚！人在塔在！')
# file.close()
#
# file1 = open('python基础班文件夹/gai_lun.txt','r',encoding='utf8')
# file2 = open('gai_lun副本.txt','w',encoding='utf-8')
# content = file1.read()
# file2.write(content)
# file2.close()
# file1.close()
