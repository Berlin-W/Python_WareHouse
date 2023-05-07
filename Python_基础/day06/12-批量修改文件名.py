"""
案例：批量修改 python 目录下的文件名
1.txt -> 1.txt
2.txt -> 2.txt
3.txt -> 3.txt
"""

"""
实现思路：
1）获取 python 目录下有哪些文件
2）再将每个文件进行重命名操作
"""
import os

# 1）获取 python 目录下有哪些文件
result = os.listdir('./python')
print(result)

# 修改当前程序的工作路径
os.chdir('./python')

# 2）再将每个文件进行重命名操作
for old_name in result:
    new_name = '黑马出品-' + old_name
    # os.rename('1.txt', '1.txt') -> os.rename('./1.txt', './1.txt')
    os.rename(old_name, new_name)

    # os.rename('./python/1.txt', './python/1.txt')
    # os.rename('./python/' + old_name, './python/' + new_name)








