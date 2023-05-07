# file = open('register.txt','r',encoding='utf8')
# content = file.readlines()
# my_dict = {}
# print(type(my_dict))
# my_list = []
# for _str in content:
#     _str = _str.strip('\n')
#     str1 = _str.split(',')
#     my_dict ={'name':str1[0],'pwd':str1[1]}
#     my_list.append(my_dict)
# print(my_list)
# file.close()



# file = open('num.txt','r',encoding='utf8')
# content = file.readlines()
# my_list = []
# for _list in content:
#     str1=_list.strip('\n')
#     str2 = eval(str1)
#     my_list.append(str2)
# print(my_list)



# user_dict = {'name': 'smart', 'age': 18, 'tel': '13888888888'}
# file = open('user.txt','w',encoding='utf8')
# _str = ''
# for key,value in  user_dict.items():
#     value = str(value)
#     _str = key +':'+ value + '\n'
#     file.write(_str)


# age = int(input('请输入年龄:'))
# if age >= 18:
#     print('欢迎来到网吧')
#     money = int(input('请输入会员卡余额:'))
#     if money > 0:
#         print('可以上网了')
#     else:
#         print('需要充值')
# else:
#     print('满18岁才能进入')




alpha_list = ['A', 'B', 'C', 'A', 'B', 'B']
data = {}
for list1 in alpha_list:
    data[list1] = alpha_list.count(list1)
for key,value in data.items():
    print(f'字母:{key} 频次:{value}')
