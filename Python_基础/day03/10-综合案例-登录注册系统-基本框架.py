"""
登录注册系统
"""
"""
数据存储的分析：
1）如何保存单个注册用户的信息？
  用户名/ 密码
2）如果保存多个注册用户的信息？

案例功能的分析：

"""
# user_list = [{'name':'smart','pwd':'123abc*'},{'name':'linda','pwd':'123456abc'}]

# # 遍历user_list,遍历出来的每一个数据都是字典
# for user in user_list:
#     print(type(user),user)
#     # 遍历出每个字典时,获取每个字典的用户名,密码
#     print(user['name'],user['pwd'])


# 需求:先实现一个简单的程序框架
# 1.提示用户输入功能数字
# while True:
#     print(user_list)
#     cmd_num = int(input('请输入操作:  1.用户注册/ 2.用户登录/ 3.退出程序: '))
#     if cmd_num == 1:
#
#         # 思考:实现用户注册功能的同时,要求用户名不允许重复
#         # 1.提示用户输入注册的用户名
#         # 2.判断新注册的用户名和老用户名是否存在相同 (遍历列表,获取老用户的注册信息和新用户比较)
#
#         # 如果不存在同名的用户,继续提示输入用户名 密码
#         _name = input('请输入注册的用户名:')
#         for user in user_list:
#             # 如果存在同名的用户,则提示:该用户已经在!不能重复注册
#             if user['name'] == _name:
#                 print('该用户已存在,不能重复注册!')
#                 break
#         # 如果不存在同名的用户,继续提示输入用户名 密码存放到一个字典中,然后将字典放入列表中
#         else:
#             _pwd = input('请输入注册的密码:')
#             user_dict = {'name':_name,'pwd':_pwd}
#             user_list.append(user_dict)
#             print('注册成功')
#
#     elif cmd_num == 2:
#         # 提示用户输入用户名和密码
#         _name = input('请输入登录的用户名:')
#         _pwd = input('请输入登录的密码:')
#         # 判断输入的用户名和密码 和 字典中的用户名和密码 比对
#         for user_info in user_list:
#             if user_info['name'] == _name and user_info['pwd'] == _pwd:
#                 print('登录成功!')
#                 break
#         else:
#             print('用户名或密码错误,请重新输入!')
#
#     elif cmd_num == 3:
#         print('退出程序')
#         break
#     else:
#         # 如果不存在,就提示:用户名或密码错误
#         print('输入有误!请重试新输入!')

user_list = [{'name':'smart','pwd':'123abc*'},{'name':'linda','pwd':'123456abc'}]
# 2.判断用户输入的数字,执行相应的操作
while True:
    cmd_num = input("请输入操作：1、用户注册/2、用户登录/3、退出系统(1/2/3):")
    if cmd_num == '1':
        user_name = input("请输入用户名：")
        for user in user_list:
            if user['name'] == user_name:
                print("该用户名已经存在，请重新注册！")
                break
        else:
            password = input("请输入密码：")
            user_dict = {'name':user_name,'pwd':password}
            user_list.append(user_dict)
            print('注册成功！')

    elif cmd_num == '2':
        _name = input("请输入用户名：")
        _password = input("请输入密码：")
        print(user_list)
        for user_info in user_list:
            if user_info['name'] == _name and user_info['pwd'] == _password:
                print('登陆成功！')
                break
        else:
            print('用户名或密码错误！')

    elif cmd_num == '3':
        print("退出系统！")
        break
    else:
        print("请输入正确的数字(1/2/3)！")








