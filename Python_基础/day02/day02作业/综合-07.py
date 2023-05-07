user_name = 'aaa'
password = '123456'
msg = 'qwer'
if msg == 'qwer':
    print('验证码正确')
    if user_name == 'aaa'and password == '123456':
        print('用户名,密码正确,成功登录!')
    else:
        print('用户名,密码错误')
else:
    print('验证码错误,登录失败')
