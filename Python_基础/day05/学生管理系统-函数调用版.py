"""
数据存储的分析：
1）如何保存一个学生的信息(姓名、年龄、电话)？
  使用 字典去保存一个学生信息
  {'name':'smart','age':18,'tel':'185'}
  {'name':'linda','age':16'tel':'138'}

2）如何保存多个学生的信息？
    使用列表套字典,列表中的每个数据都是字典
    [{'name':'smart','age':18,'tel':'185'},
    {'name':'linda','age':16'tel':'138'}]


案例功能分析：
1)显示功能菜单
2)查询所有学生
3)查询所有学生
4)修改某个学生
5)删除某个学生
6)删除某个学生
7)退出系统

"""
user_list = [{'name':'smart','age':18,'tel':'135'},
             {'name':'linda','age':16,'tel':'138'}]

#  函数定义:定义一个函数,名字叫show_menu(),打印功能菜单
def show_menu():
    """打印功能菜单"""
    print('= 1.添加学生')
    print('= 2.查询所有学生')
    print('= 3.查询某个学生')
    print('= 4.修改某个学生')
    print('= 5.删除某个学生')
    print('= 6.退出系统')

# 添加学生函数
def add_stu():
    stu_name = input('请输入学生姓名:')
    for stu_info in user_list:
        if stu_name == stu_info['name']:
            print('输入的学生名字存在，不允许重复添加！')
            '''如果找到重名的同学，就结束遍历'''
            break
    # 如果没不存在重名的同学，重新输入
    else:
        stu_name = input('请重新输入学生姓名:')

    stu_age = int(input('请输入学生年龄:'))
    # 对输入的年龄进行合法判断
    if stu_age < 0 or stu_age > 100:
        print('输入的年龄不合法!,请重新输入!')
        stu_age = int(input('请输入学生年龄:'))

    stu_tel = input('请输入学生手机号:')
    stu_dict = {'name': stu_name, 'age': stu_age, 'tel': stu_tel}
    print('===========================================')
    print(f'您输入的信息为:  姓名:{stu_name} 年龄:{stu_age}  电话:{stu_tel}')
    user_list.append(stu_dict)
    print('===========================================')

# 查询所有学生函数
def query_all_stu():
    print('学生信息如下:')
    print('===========================================')
    for i in user_list:
        print(i)
    print('===========================================')

# 查询某个学生参数
def query_stu():
    search_name = input('请输入想要查询的学生姓名:')
    for stu in user_list:
        if search_name == stu['name']:
            print(f'您查询的 {search_name} 的信息如下: ')
            print('===========================================')
            print(stu)
            print('===========================================')
            break
    else:
        print('===========================================')
        print('查无此人! 请返回主页面重新操作!')
        print('===========================================')

# 修改学生函数
def change_stu():
    change_stu_name = input('请输入想要修改的学生姓名:')
    for stu in user_list:
        if change_stu_name == stu['name']:
            change_stu_age = input('请输入修改后的年龄:')
            change_stu_tel = input('请输入修改后的电话:')
            stu['age'] = change_stu_age
            stu['tel'] = change_stu_tel
            print(f'修改后的 {change_stu_name} 的信息如下:')
            print('===========================================')
            print(stu)
            print('===========================================')
            break
    else:
        print('===========================================')
        print('查无此人! 请返回主页面重新操作!')
        print('===========================================')


# 删除学生函数
def delete_stu():
    del_stu_name = input('请输入想要删除的学生姓名:')
    i = 0
    for index, del_stu in enumerate(user_list):
        if del_stu_name == del_stu['name']:
            del user_list[index]
            print('删除成功!')
            break
    else:
        print(f'删除失败,没有 {del_stu_name} 的学生信息!')

def exit_system():
    print('退出系统')

def main():
    """ 学生名片管理系统的主题逻辑"""
    while True:
        # ① 打印显示的功能菜单
        show_menu()
        # ② 接收用户的输入
        cmd_num = input('请输入功能数字:')

        # print('添加学生')
        if cmd_num == '1':
           add_stu()

        # print('查询所有学生')
        elif cmd_num == '2':
           query_all_stu()

        # print('查询某个学生')
        elif cmd_num == '3':
            query_stu()

        # print('修改某个学生')
        elif cmd_num == '4':
            change_stu()

        # print('删除某个学生')
        elif cmd_num == '5':
            delete_stu()


        elif cmd_num == '6':
           exit_system()
        else:
            print('输入有误!请重新输入!')

main()
