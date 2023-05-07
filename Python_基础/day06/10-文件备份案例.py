"""
文件备份案例需求：
    比如有一个文件 abc.abc.txt，备份之后的文件名为：abc.abc[备份].txt

    abc.abc.txt -> abc.abc[备份].txt
        abc.abc + [备份] + .txt
    xxx.txt -> xxx[备份].txt
        xxx + [备份] + .txt
"""

"""
文件备份的思路分析：【读取旧文件内容，写入到新文件】
1）只读模式打开旧文件，只写模式打开新文件
2）读取旧文件内容，写入到新文件
3）关闭旧文件和新文件
"""


# # 提示用户输入要备份的文件名称
# old_name = input('请输入要备份的文件名称：')
#
# # 根据输入 old_name 生成备份的文件名称：new_name
# index = old_name.rfind('.') # rfind：字符串从后向前找第一个出现.，把它的下标返回
# new_name = old_name[:index] + '[备份]' + old_name[index:]
# print(new_name)
#
# # 1）只读模式打开旧文件，只写模式打开新文件
# old_file = open(old_name, 'r', encoding='utf8')
# new_file = open(new_name, 'w', encoding='utf8')
#
# # 2）读取旧文件内容，写入到新文件
# content = old_file.read()
# new_file.write(content)
#
# # 大文件内容的读取
# while True:
#     # 每次循环从旧文件中读取一小部分内容
#     content = old_file.read(4)
#
#     # 判断是否读取到了文件的末尾，如果读到了末尾，循环结束
#     if content == '':
#         break
#
#     # 将读取一小部分内容写入到新文件中
#     new_file.write(content)
#
# # 3）关闭旧文件和新文件
# old_file.close()
# new_file.close()

old_name = input('请输入文件名：')
# 找到最后一个点出现的位置索引
index = old_name.rfind('.')
new_name = old_name[0:index] + '[备份]' + old_name[index:]
print(new_name)

old_file = open(old_name,'r',encoding='utf8')
new_file = open(new_name,'a',encoding='utf8')

# content = old_file.read()
# new_file.write(content)
# 大文件备份：每次从旧文件中读取一小部分内容，边读编写，知道文件读完
# 利用循环的办法 一直读取文件内容
while True:
    content = old_file.read(1)
    if content == '':
        break
    new_file.write(content)

old_file.close()
new_file.close()