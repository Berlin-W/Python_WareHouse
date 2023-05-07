age = int(input('请输入年龄:'))
if age > 18:
    print('允许上网')
elif age > 17:
    print('过两天再来上网')
elif age > 12:
    print('存两年钱再来上网')
else:
    print('小屁孩还敢来网吧,一会告诉你妈去')