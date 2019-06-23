import requests
import json



#json.loads():将json字符串->字典格式
#json.dunps():将字典->json字符串
#json.load(): 将json文件->字典
#json.dump(): 将字典->json文件

# req ={
#     'methon':'post',
#     'url':'http://115.28.108.130:8080/gasStation/process',
#     'json':{'dataSourceId': 'bHRz', 'methodId': '00A', 'CardInfo': {'cardNumber': 123456}}
# }
#
# f= open('1.json', 'w')
# json.dump(req, f)
# res = requests.request(**req)
# print(res.json())

# f= open('1.json')
# req = json.load(f)
# print(req,type(req))
# f.close()

f= open('2.json')
req = json.load(f)
print(req,type(req))
f.close()

f= open('2.json', 'w')
json.dump(req, f)
res = requests.request(**req)
print(res.json())


with open(2.json,encoding='utf-8') as f:
    req_list = json.load(f)

for req in req_list:
    res= requests.request(**req)
    print(req, type(req))
