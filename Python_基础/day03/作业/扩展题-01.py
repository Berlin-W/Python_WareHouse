product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]
_sum = 0
for item in product:
    money=item['price']
    _sum += money
print(_sum)
if _sum < 8000:
    print('能')
else:
    print('不能')
