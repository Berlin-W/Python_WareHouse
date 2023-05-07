age = int(input('请输入你的年龄:'))
while age < 0 or age >99 :
    print('输入的年龄不合法,请重新输入!')
    age = int(input('请输入你的年龄:'))
if age < 17:
    print(f'您的年龄是{age}:青少年')
elif age < 35:
    print(f'您的年龄是{age}:青年')
elif age < 59:
    print(f'您的年龄是{age}:中年')
else:
    print(f'您的年龄是{age}:老年')