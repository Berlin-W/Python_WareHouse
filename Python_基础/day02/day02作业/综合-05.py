# ticket取值为1表示有票，取值为0表示无票
ticket = int(input('是否有票:(1.有票 0.无票):'))
if ticket == 1:
    print('可以上车')
    seat = int(input('是否有座:(1.有座 0.无座):'))
    if seat == 1:
        print('有座位')
    else:
        print('无座位')
else:
    print('无票')
