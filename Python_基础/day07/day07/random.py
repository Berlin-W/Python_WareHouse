# 需求：随机生成一个1-10之间的数字
# 这里其实导入的是当前目录下的 random 模块
import random
# 当前目录下的 random 模块中是没有 randint 函数
num = random.randint(1, 10)
print(num)