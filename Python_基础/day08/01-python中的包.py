"""
python中包：
学习目标：知道包其实就是包含多个py模块的一个目录
"""

"""
Python中包的概念：
1）把有联系的多个模块文件，放到同一个文件夹下，并且在这个文件夹创建一个名字为__init__.py 文件，
那么这个文件夹就称之为包
2）包的本质就是一个文件夹，包的作用将模块文件组织起来
3）包能有效避免模块名称冲突问题，提高程序的结构性和可维护性
"""


"""
包的使用：
学习目标：能够通过 `import` 或 `from ... import ...` 的方法使用包中的内容
"""

"""
方式1：import 包名.模块名
    使用形式：包名.模块名.要使用的内容

方式2：from 包名 import 模块名
    使用形式：模块名.要使用的内容
    
方式3：from 包名.模块名 import 要使用的内容
    使用形式：要使用的内容
"""
# 方法1 import 包名.模块名
# import msg.send_msg,msg.recv_msg  # 导入包的时候自动输出__init__.py的内容
# msg.send_msg.send_msg()
# msg.recv_msg.recv_msg()
#
# print('====================')
# # 方法2 from 包名 import 模块名
# from  msg import send_msg,recv_msg
# send_msg.send_msg()
# recv_msg.recv_msg()
#
# print('====================')
# # 方法3 from 包名.模块名 import 要使用的内容
# from msg.send_msg import send_msg
# from msg.recv_msg import  recv_msg
# send_msg()
# recv_msg()





"""
包目录中 __init__.py 文件的作用
学习目标：了解包目录下 __init__.py 文件的作用
"""
import msg
msg.recv_msg.recv_msg()
msg.send_msg.send_msg()


