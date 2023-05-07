# 学生名片管理系统
"""
业务解读:
    1.循环打印菜单
    2.学生信息以字典的形式存放到 user_List列表中

"""
# 定义学生信息
user_list = [{'name': 'mike', 'age': 34, 'tel': '110'},
             {'name': 'yoyo', 'age': 18, 'tel': '120'}]
while True:
    print("* " * 20)
    print('= 1. 添加学生')
    print('= 2. 查询所有学生')
    print('= 3. 查询某个学生')
    print('= 4. 修改某个学生')
    print('= 5. 删除某个学生')
    print('= 6. 退出系统')
    print("* " * 20)
    operation = input("请输入操作:")
    if operation == '1':
        user_name = input("请输入添加的学生姓名:")
        for user in user_list:
            if user_name == user["name"]:
                print("您输入的用户名已存在!")
                break
        else:
            age = int(input("请输入学生的年龄:"))
            phone = input("请输入学生的联系方式:")
            # 将输入的信息存放为字典
            user_dict = {'name': user_name, 'age': age, 'tel': phone}
            # 将字典添加到user_list的列表中
            user_list.append(user_dict)

    # 查询所有学生信息
    if operation == '2':
        print("-" * 30)
        for i,user in enumerate(user_list):
            print(f"姓名:{user['name']}\t年龄:{user['age']}\t电话:{user['tel']}")
        print("-" * 30)
    # 查询某个学生信息
    if operation == '3':
        query_stu_name = input("请输入查询的学生姓名:")
        for user in user_list:
            # 查到了,就返回学生的全部信息
            if query_stu_name == user['name']:
                print(f"姓名:{user['name']}\t年龄:{user['age']}\t电话:{user['tel']}")
                break
        else:
            print("查无此人!")
    # 修改学生信息
    if operation == '4':
        # 修改学生之前,先查询有没有这个学生
        update_stu_name = input("请输入修改的学生姓名:")
        for user in user_list:
            if update_stu_name == user['name']:
                while True:
                    update_stu_age = int(input("请输入修改后的年龄:"))
                    if 0 <= update_stu_age <= 100:
                        update_stu_tel = input("请输入修改后的电话:")
                        break
                    else:
                        print("输入年龄不合法,请重新输入~")
                user['age'] = update_stu_age
                user['tel'] = update_stu_tel
                break
        else:
            print("系统不存在该学生!")
    # 删除学生信息
    if operation == '5':
        delete_stu_name = input("请输入想要删除的学生姓名:")
        # 删除之前,先校验有没有这个学生
        for i,user in enumerate(user_list):
            if user['name'] == delete_stu_name:
                # user_list.remove(user)
                del user_list[i]
                break
        else:
            print("查无此人!")
    # 退出系统
    if operation == '6':
        print("退出系统!")
        break


