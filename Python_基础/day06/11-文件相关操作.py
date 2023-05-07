"""
os模块：python中进行文件、目录相关操作的模块(工具包)
"""
# 导入工具包
import os

"""
os模块中的rename()可以完成对文件的重命名操作
语法格式：os.rename(旧的文件名，新的文件名)
"""

# os.rename('xxx.txt', 'xxx-最终版.txt')


"""
os模块中的remove()可以完成对文件的删除操作，不能删除文件夹
语法格式：os.remove(待删除的文件名)
"""

# os.remove('xxx[备份].txt')


"""
创建文件夹，只能创建文件夹，不能创建普通文件
语法格式：os.mkdir(文件夹的名字)
"""

# os.mkdir('python')


"""
删除文件夹，只能删除空的文件夹
语法格式：os.rmdir(待删除文件夹的名字)
"""

# os.rmdir('python')


"""
获取当前工作的路径
语法格式：路径变量 = os.getcwd() # cwd：current working directory
"""

# 获取当前程序的工作路径，默认的工作路径就是当前执行 python 文件所在的目录
# 绝对路径：C:\Users\smart\Desktop\pycode\day06
result = os.getcwd()
print(result)


"""
改变默认目录，切换指定的路径
语法格式：os.chdir(改变的路径) # ch：change 改变
"""
# 改变当前程序的工作目录
# os.chdir('python')
#
# result = os.getcwd()
# print(result)
#
# # 【注意：在 python 程序中，相对路径都是基于程序工作目录而言的】
# with open('./1.txt', 'w') as f:
#     f.write('111111')

"""
获取某个目录的文件信息，获取文件夹或文件的名字
语法格式：目录列表变量 = os.listdir(指定某个目录)
如果不指定目录，默认当前路径
"""
result = os.listdir('.')
print(result)

"""
语法格式：os.path.exists(需要判断的文件)
如果文件存在返回True，如果文件不存在返回False
"""

result = os.path.exists('./python/2.txt')
print(result)



