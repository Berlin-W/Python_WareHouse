
import time

m = 0
while m < 60:  # 每小时,需要执行60次分针移动
    s = 0
    while s < 60:  # 每分钟,需要执行60次秒针移动
        print("%02d:%02d" % (m, s))
        time.sleep(1)
        s += 1
    m += 1