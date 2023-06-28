# 将其他数据转换为json
import json

data = [{"name": "张三", "age": 14}, {"name": "李四", "age": 15}, {"name": "王五", "age": 16}]

mydata1 = json.dumps(data, ensure_ascii=False);

print(mydata1)

# 将json数据转换为其他数据类型
s = ' [{"name": "张三", "age": 14}, {"name": "李四", "age": 15}, {"name": "王五", "age": 16}]'
json.loads(s)
print(type(s))
print(s)