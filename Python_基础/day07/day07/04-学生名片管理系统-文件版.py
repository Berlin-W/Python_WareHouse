"""
数据存储的分析：
1）如何保存一个学生的信息(姓名、年龄、电话)？字典
    学生1：{'name': 'smart', 'age': 18, 'tel': '135'}
    学生2：{'name': 'linda', 'age': 16, 'tel': '138'}

2）如何保存多个学生的信息？列表套字典：列表中的每个数据都是一个字典
    [{'name': 'smart', 'age': 18, 'tel': '135'}, {'name': 'linda', 'age': 16, 'tel': '138'}, ...]

案例功能分析：
1）显示功能菜单，接收用户的输入
2）添加学生
3）查询所有学生
4）查询某个学生
5）修改某个学生
6）删除某个学生
7）退出系统
"""

# 先定义一个列表 user_list，假设已经有两个学生了
# 全局变量
user_list = []


# 函数定义：定义一个函数，名字叫 show_menu，打印功能菜单
def show_menu():
    """打印功能菜单"""
    print('= 1. 添加学生')
    print('= 2. 查询所有学生')
    print('= 3. 查询某个学生')
    print('= 4. 修改某个学生')
    print('= 5. 删除某个学生')
    print('= 6. 退出系统')


# 定义一个函数：add_stu_info，把添加学生的代码封装进去
def add_stu_info():
    """添加学生的代码"""
    # ① 提示用户输入要添加学生的姓名
    _name = input('请输入学生姓名：')

    # ② 遍历已有的学生的数据，判断新添加学生姓名和已有的学生姓名是否存在相同
    for user in user_list:
        if user['name'] == _name:
            # 如果存在同名的学生，则提示：该同学已存在！不允许重复添加！
            print('该同学已存在！不允许重复添加！')
            break
    else:
        # 如果不存在同名的学生，则提示用户输入学生的年龄和电话，然后将学生的信息保存成一个字典，再将字典添加到列表中
        _age = int(input('请输入学生的年龄：'))  # str -> int
        _tel = input('请输入学生的电话：')

        # 将学生的信息保存成一个字典
        user_dict = {'name': _name, 'age': _age, 'tel': _tel}

        # 再将字典添加到列表中
        # 注意：这里并不是对 user_list 赋值：user_list = 数据
        user_list.append(user_dict)


# 定义一个函数：show_all_stu，把显示所有学生的代码放进去
def show_all_stu():
    """显示所有学生的数据"""
    print('序号\t\t姓名\t\t年龄\t\t电话')
    # 遍历 user_list 学生数据的列表，获取每个学生的数据并进行打印显示
    for i, user in enumerate(user_list):
        # \t: 制表符，相等于按了一下 tab 键
        print(f'{i}\t\t{user["name"]}\t\t{user["age"]}\t\t{user["tel"]}')


# 定义一个函数：show_one_stu，把查询某个学生的代码放进去
def show_one_stu():
    """查询某个学生的数据"""
    # ① 提示用户输入要查找的学生姓名
    _name = input('请输入学生姓名：')

    # ② 遍历 user_list，获取每个学生的信息，判断学生的姓名和要查找的学生姓名是否相同
    for i, user in enumerate(user_list):
        # 如果找到学生，则显示对应学生的信息
        if user['name'] == _name:
            print('序号\t\t姓名\t\t年龄\t\t电话')
            print(f'{i}\t\t{user["name"]}\t\t{user["age"]}\t\t{user["tel"]}')
            break
    else:
        # 如果找不到学生，则提示：查无此人！该学生不存在！
        print('查无此人！该学生不存在！')


# 定义一个函数：update_one_stu，把修改学生的代码放进去
def update_one_stu():
    """修改某个学生的数据"""
    # ① 提示用户输入要修改的学生姓名
    _name = input('请输入学生姓名：')

    # ② 遍历 user_list，根据输入的姓名查询要修改的学生
    for user in user_list:
        # 如果学生存在，则提示用户输入修改之后的姓名、年龄和电话，然后进行修改
        if user['name'] == _name:
            # 提示用户输入修改之后的姓名、年龄和电话
            new_name = input('请输入修改之后的姓名：')
            new_age = int(input('请输入修改之后的年龄：'))  # str -> int
            new_tel = input('请输入修改之后的电话：')

            # 然后进行修改(其实就是修改字典的key对应的值)
            user['name'] = new_name
            user['age'] = new_age
            user['tel'] = new_tel
            break
    else:
        # 如果学生不存在，则提示：查无此人！该学生不存在！
        print('查无此人！该学生不存在！')


# 定义一个函数：delete_one_stu，将删除学生的代码放进来
def delete_one_stu():
    """删除某个学生的数据"""
    # ① 提示用户输入要删除的学生的姓名
    _name = input('请输入学生姓名：')

    # ② 遍历 user_list，根据输入的姓名查询要删除的学生
    for i, user in enumerate(user_list):
        # 如果学生存在，则将对应学生的数据(也就是字典)从列表中删除
        if user['name'] == _name:
            del user_list[i]
            print('学生信息删除成功！')
            break
    else:
        # 如果学生不存在，则提示：操作失败！该学生不存在！
        print('操作失败！该学生不存在！')


# 定义一个函数：save_data，将学生的数据保存到文件中
def save_data():
    """将学生的数据保存到文件中"""
    # 将 user_list 中添加的学生数据全部写入到 stu.txt 文件中
    with open('./stu.txt', 'w', encoding='utf8') as f:
        # 先将 user_list 列表转换为一个字符串
        content = str(user_list)
        f.write(content)


# 定义一个函数：load_data，从文件中读取学生的全部数据
def load_data():
    """从文件中读取学生的全部数据"""
    # 首先判断 stu.txt 文件是否存在
    import os
    # if not False -> if True
    if not os.path.exists('./stu.txt'):
        print('stu.txt文件不存在！')
        return

    with open('./stu.txt', 'r', encoding='utf8') as f:
        # 读取文件的全部内容
        content = f.read()  # str
        # 将读取到的学生数据赋值给 user_list
        global user_list  # 告诉 python 解释器，接下来要使用的 user_list 是全局变量
        user_list = eval(content)  # eval(content)：str -> list


# 函数定义：定义一个函数，名字叫 main，把学生名片管理系统的主体逻辑代码放进去
def main():
    """学生名片管理系统主体逻辑代码"""
    # 从 stu.txt 文件中读取学生的全部数据
    load_data()

    while True:
        print(user_list)
        # ① 打印显示功能菜单
        show_menu()

        # ② 接收用户的输入
        cmd_num = input('请输入功能数字：') # str

        # ③ 根据用户的输入，判断用户要进行的操作
        if cmd_num == '1':
            # print('添加学生')
            # 调用添加学生的函数
            add_stu_info()
        elif cmd_num == '2':
            # print('查询所有学生')
            show_all_stu()
        elif cmd_num == '3':
            # print('查询某个学生')
            show_one_stu()
        elif cmd_num == '4':
            # print('修改某个学生')
            update_one_stu()
        elif cmd_num == '5':
            # print('删除某个学生')
            delete_one_stu()
        elif cmd_num == '6':
            print('退出系统')
            # 调用学生数据保存到文件中的函数
            save_data()
            # 终止循环
            break
        else:
            print('输入有误！请重新输入！')


# 函数调用：调用 main 函数
main()
