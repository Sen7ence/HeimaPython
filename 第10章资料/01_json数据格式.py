"""
演示JSON数据和Python字典的相互转换
"""

import json  # 导入json模块

# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [
    {"name": "张大帅", "age": 11},
    {"name": "王大锤", "age": 13},
    {"name": "赵小虎", "age": 16},
]
json_str = json.dumps(data, ensure_ascii=False)# 将Python对象转换为JSON字符串，ensure_ascii=False表示不转义中文字符
print(type(json_str))  # <class 'str'>
print(json_str)

# 准备字典，转换为JSON
data = {"name": "周杰轮", "addr": "台北"}
json_str = json.dumps(data, ensure_ascii=False)  # 将Python对象转换为JSON字符串，ensure_ascii=False表示不转义中文字符
print(type(json_str))  # <class 'str'>
print(json_str)  # {"name": "周杰轮", "addr": "台北"}

# 准备JSON字符串，转换为Python对象
s = '[{"name": "张大帅", "age": 11},{"name": "王大锤", "age": 13},{"name": "赵小虎", "age": 16}]'
l = json.loads(s)  # 将JSON字符串转换为Python对象
print(type(l))  # <class 'list'>
print(l)  # [{'name': '张大帅', 'age': 11}, {'name': '王大锤', 'age': 13}, {'name': '赵小虎', 'age': 16}]

# 准备JSON字符串，转换为Python对象
s = '{"name": "周杰轮", "addr": "台北"}'
d = json.loads(s)  # 将JSON字符串转换为Python对象
print(type(d))  # <class 'dict'>
print(d)  # {'name': '周杰轮', 'addr': '台北'}