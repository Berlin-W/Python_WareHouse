height = float(input('请输入你的身高(m):'))
weight = int(input('请输入你的体重(kg):'))
BMI = float(weight / height ** 2)
print(BMI)
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')
