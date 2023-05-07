
_str = input("请输入一个字符串：")
for i in _str:
    if i == "q":
        break
    elif i == " ":
        continue
    print(i)