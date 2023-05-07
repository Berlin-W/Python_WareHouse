"""
案例：批量修改 python 目录下的文件名
1.txt -> 黑马出品-1.txt
2.txt -> 黑马出品-2.txt
3.txt -> 黑马出品-3.txt
"""

"""
实现思路：
① 获取python目录下的文件内容
② 遍历修改每个文件的文件名
③ 

"""
# ① 获取python目录下的文件内容
import os


# os.listdir()获取当前目录的文件名
result = os.listdir('./python')
res = os.chdir('./python')
# ② 遍历修改每个文件的文件名
for old_name in result:
    # 生成新的文件名
    new_name = '黑马出品-' + old_name
    #  os.rename()对文件重命名
    os.rename(old_name,new_name)
