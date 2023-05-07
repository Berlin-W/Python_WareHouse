a = {'i','t','h','e','m','a'}
_str = input('输入一个字母:')
for i in a:
    if _str == i:
        print('找到了')
        break
else:
    print('查无此字母')