"""
案例：批量修改 python 目录下的文件名
1.txt -> 黑马出品-1.txt
2.txt -> 黑马出品-2.txt
3.txt -> 黑马出品-3.txt
"""

"""
实现思路：
① 首先获取 python 目录有哪些文件
② 遍历去修改每个文件的文件名
"""
import os

# ① 首先获取 python 目录有哪些文件
result = os.listdir('./python')
# print(result) # 列表：['1.txt', '2.txt', '3.txt']

# 切换当前运行程序的工作路径
os.chdir('./python')

# ② 遍历去修改每个文件的文件名
for old_name in result:
    # 生成新文件名
    new_name = '黑马出品-' + old_name
    # 对每个文件进行重命名
    # os.rename('1.txt', '黑马出品-1.txt') -> os.rename('./1.txt', './黑马出品-1.txt')
    os.rename(old_name, new_name)
