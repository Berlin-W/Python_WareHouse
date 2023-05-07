num1 = int(input('请输入一个数字:'))
sign = input('请输入一个操作符:')
num2 = int(input('请输入第二个数字:'))
res = 0
if sign == '+':
    res = num2 + num1
elif sign == '-':
    res = num1 - num2
elif sign == '*':
    res = num2 * num1
else:
    res = num1 / num2
print(res)