"""
获取当前运行程序的工作路径，默认就是当前程序文件所在目录
语法格式：路径变量 = os.getcwd() # cwd：current working directory
"""
import os

result = os.getcwd()
print(result)



"""
改变运行程序的工作目录，切换指定的路径
语法格式：os.chdir(改变的路径) # ch：change 改变
"""

# 将当前程序的工作路径改成 python
os.chdir('./python')
result = os.getcwd()
print(result)


"""
运行程序工作路径意义：程序中使用的相对路径都是基于工作路径而言的
"""

# .：指当前程序的工作路径
# ..：当前程序工作路径的上层目录
with open('./xxx.txt', 'w', encoding='utf8') as f:
    f.write('xxx')

