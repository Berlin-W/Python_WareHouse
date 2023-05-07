"""
数据存储的分析：
1）如何保存一个学生的信息(姓名、年龄、电话)？字典
    用户1 => {'name': 'smart', 'age': 18, 'tel': '131'}
    用户2 => {'name': 'linda', 'age': 16, 'tel': '133'}
2）如何保存多个学生的信息？列表嵌套字典
    [{'name': 'smart', 'age': 18, 'tel': '131'},
    {'name': 'linda', 'age': 16, 'tel': '133'}, ...]

案例功能分析：
1）显示菜单，提示用户输入功能数字
2）添加学生
3）查询所有学生
4）查询一个学生
5）修改一个学生
6）删除一个学生
7）退出系统
"""

# 全局变量
stu_list = [{'name': 'smart', 'age': 18, 'tel': '131'}, {'name': 'linda', 'age': 16, 'tel': '133'}]


# 定义一个函数，功能是显示菜单
def show_menu():
    """显示功能菜单"""
    print('= 1. 添加学生')
    print('= 2. 查询所有学生')
    print('= 3. 查询某个学生')
    print('= 4. 修改某个学生')
    print('= 5. 删除某个学生')
    print('= 6. 退出系统')


# 定义一个函数，实现添加学生功能
def add_stu_info():
    """添加学生"""
    # ① 提示用户输入要添加的学生的姓名
    name = input('请输入学生姓名：')

    # ② 判断添加的学生姓名是否已经存在
    for stu_dict in stu_list:
        if stu_dict['name'] == name:
            # 如果已存在，则提示：该学生已存在！不能重复添加！
            print('该学生已存在！不能重复添加！')
            break
    else:
        # 如果不存在，再提示用户输入要添加的学生的年龄和电话，将学生的数据保存到字典中，然后将字典添加到列表中
        age = int(input('请输入学生年龄：'))  # str -> int
        tel = input('请输入学生电话：')

        # 将学生的数据保存到字典中
        new_stu = {'name': name, 'age': age, 'tel': tel}

        # 然后将字典添加到列表中
        stu_list.append(new_stu)
        print(f'{name}学生添加成功！')


def show_all_stu():
    """显示所有学生"""
    print('序号\t\t姓名\t\t年龄\t\t电话')
    # 1. 遍历 stu_list 列表，显示每个学生的信息
    for i, stu_dict in enumerate(stu_list):
        # \t：制表符
        print(f'{i}\t\t{stu_dict["name"]}\t\t{stu_dict["age"]}\t\t{stu_dict["tel"]}')


def show_one_stu():
    """显示一个学生"""
    # ① 提示用户输入要查询的学生姓名
    name = input('请输入学生姓名：')

    # ② 根据输入的学生姓名，遍历 stu_list 列表，来查询对应的学生数据
    for i, stu_dict in enumerate(stu_list):
        if stu_dict['name'] == name:
            # 如果查询到学生，则显示学生的信息
            print('序号\t\t姓名\t\t年龄\t\t电话')
            print(f'{i}\t\t{stu_dict["name"]}\t\t{stu_dict["age"]}\t\t{stu_dict["tel"]}')
            break
    else:
        # 如果查询不到学生，就提示：查无此人，没有学生信息！
        print(f'查无此人，没有学生{name}信息！')


def main():
    """主函数"""
    while True:
        print(stu_list)
        # 1. 显示功能菜单
        # 调用 show_menu 函数
        show_menu()

        # 2. 提示用户输入功能数字
        cmd_num = input('请输入功能数字：')

        # 3. 根据用户输入的功能数字判断执行什么操作
        if cmd_num == '1':
            # print('添加学生')
            add_stu_info()
        elif cmd_num == '2':
            # print('查询所有学生')
            show_all_stu()
        elif cmd_num == '3':
            # print('查询某个学生')
            show_one_stu()
        elif cmd_num == '4':
            print('修改某个学生')
        elif cmd_num == '5':
            print('删除某个学生')
        elif cmd_num == '6':
            print('退出系统！')
            break
        else:
            print('输入有误！请重新输入！')


# 调用 main 函数
main()
