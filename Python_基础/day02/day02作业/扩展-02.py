run_year = int(input('输入一个年份:'))
if (run_year % 4 == 0 and run_year % 100 != 0) or run_year % 400 ==0:
    print(f'{run_year}是闰年')
else:
    print(f'{run_year}不是闰年')