info={}
info={'name':'张三'}
print(info)
print(info.get('name'))
info['name']='李四'
print(info.get('name'))
info.pop('name')
print(info.get('name'))
