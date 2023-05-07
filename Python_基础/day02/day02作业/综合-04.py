num1 = int(input('请输入第一个数字:'))
num2 = int(input('请输入第二个数字:'))
num3 = int(input('请输入第三个数字:'))
_sum = num1 + num2 + num3
if _sum > 100000 :
    print('您输入的三位数的和忒大了')
elif _sum > 10000 :
    print('您输入的三位数的和挺大')
elif _sum >1000:
    print('您输入的三位数的和有点大')
elif _sum > 100 or _sum < 1000 :
    print('您输入的三位数的和不算大')
else:
    print('您输入的三位数的和忒小了')

