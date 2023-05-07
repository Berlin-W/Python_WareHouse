"""
学习目标：掌握 json 模块中 dumps 和 loads 函数的使用
json.dumps(列表或字典): 将python中的列表和字典转换为符合json格式的字符串
json.loads(列表或字典):讲json格式的字符串转换python中的列表或字典
"""
import json


# data = [{'name': '老王', 'age': 16}, {'name': '张三', 'age': 20}]
# res = json.dumps(data)
# print(type(res),res)


print('====================')
json_str = '[{"name": "\u8001\u738b", "age": 16}, {"name": "\u5f20\u4e09", "age": 20}]'
res = json.loads(json_str)
print(res)