"""
模块内置变量：__name__
学习目标：能够通过模块内置变量 __name__ 解决模块测试代码被执行的问题
"""

"""
模块内置变量：__name__

在 Python 中的每个模块都有一个 __name__ 内置变量，该内置变量的值在以下2种情况时不同：

比如现在有 1 个模块：smart.py

1）若是直接运行 smart.py 的代码，在其中获取 smart 模块的 __name__，它的值是：'__main__'
2）若是另一个模块引入了 smart 模块，并且在另一个模块中获取 smart 模块的 __name__，它的值是：'smart'
"""

# 注意：
# 1）在 smart 模块中获取自己的 __name__，结果就是：__main__
# 2）在当前模块中获取 smart 模块的 __name__，结果就是：smart
import Berlin
print(Berlin.__name__) # 'Berlin'

"""
__name__ 的作用：在一个模块内容，使用如下方式为模块添加测试代码

if __name__ == '__main__':
    # 模块功能测试代码
    
注意：这样做的目的是，其他模块导入该模块时，被导入模块中的测试代码不会被执行
"""

# 注意：
# 1）直接运行 smart 模块的代码，smart 模块中的测试代码会运行
# 2）在当前模块中导入 smart 模块时，smart 模块中的代码不会运行
# import smart
import Berlin as berlin
num = berlin.my_sub(3,1)
print(num)
