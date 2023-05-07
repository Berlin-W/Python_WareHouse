"""
学习目标：能够使用 pyecharts 绘制疫情地图
"""
import json
#  读取疫情.txt中的数据
with open('疫情.txt','r',encoding='utf8') as file:
    content = file.read()  # str  这个字符串符合json数据格式

# 将读取文件数据 转化为python中的字典
res_dict = json.loads(content)  # 把json的str  转为 python的字典
# print(type(res_dict),res_dict)

# 从字典中提取省份的名称和对应的确诊人数

# print(type(res_dict["areaTree"]),res_dict["areaTree"])
# _str = res_dict["areaTree"][0].get("children")
# print(_str)

# 这个列表中每个数据 都是一个字典,一个字典就是一个省的数据
# 遍历列表 获得每个省的疫情数据 ,在提取每个省的名称和确诊人数
province_dict = {}
province_list = res_dict["areaTree"][0]["children"]
for province_info in province_list:
    province_name = province_info['name']
    province_confirm = province_info['total']['confirm']
#     将省的名称和对应的确诊人数添加到字典中,key是省的名字,value是对应的确诊人数
    province_dict[province_name]=province_confirm
# print(province_dict)

# 将 province_dict 字典的key 和对应的 value  组合到一起
# 疫情地图的要求格式:[('台湾',15880),('江苏',1576),.....]

# # 获取字典的所有的key
# print(province_dict.keys())
# # 获取字典的所有的value
# print(province_dict.values())

data1 = zip(province_dict.keys(),province_dict.values())
data = list(data1)
print(data)

# 利用data数据 结合安装的pyecharts 绘制疫情地图
# 首先创建一个地图

from pyecharts.charts import Map
visual_map = Map()
# 给地图添加数据
visual_map.add('国内疫情地图',data,'china')
# 给地图添加设置
from pyecharts import options as opts
visual_map.set_global_opts(visualmap_opts=opts.VisualMapOpts(
    is_piecewise=True,
    pieces=[
        {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
        {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
        {"min": 100, "max": 499, "label": "100-499人", "color": "#FF9966"},
        {"min": 500, "max": 999, "label": "500-999人", "color": "#FF6666"},
        {"min": 1000, "max": 9999, "label": "1000-999人", "color": "#CC3333"},
        {"min": 10000, "label": "10000以上", "color": "#990033"}
    ]
))
# 开始绘制地图
visual_map.render()
#