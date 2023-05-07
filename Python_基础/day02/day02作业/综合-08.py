money = int(input('请输入银行卡余额:'))
pay_money = int(input('请输入付款的金额:'))
key = 1 if money - pay_money >= 0 else money - pay_money
if key >= 0 :
    print('使用银行卡付款')
    print(f'卡上余额{money-pay_money}元')
else:
    print('余额不足')