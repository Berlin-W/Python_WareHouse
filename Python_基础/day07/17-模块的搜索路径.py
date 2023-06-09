"""
模块的搜索路径
学习目标：知道导入模块时 python 解释器是根据 `sys.path` 搜索模块的
"""

"""
当你导入一个模块，Python解析器对模块位置的搜索顺序是：
1）当前目录
2）如果不在当前目录，Python则搜索系统路径

注意：模块搜索路径列表存储在 sys 模块的sys.path变量中。
"""
import  sys

print(sys.path)
# ModuleNotFoundError
# No module named 'xxx'
# import xxx


# 注意：
# 当我们导入一个模块时，是按照 `sys.path` 中的目录列表，按从左到右的顺序查找指定要导入的模块，
# 1）如果前面的路径中有要导入的模块，则不会再查询后面的路径
# 2）如果每个目录下都查找不到要导入的模块，则最终会出现 ModuleNotFoundError 错误


# 提示：打开下面这句代码的注释，强制把 sys.path 设置为 []，则会发现下面的导入会出错
# sys.path = []

# from smart import *
