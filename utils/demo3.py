import xlrd
import requests
import json


wb=xlrd.open_workbook('data.xls')
sh=wb.sheet_by_name('添加加油卡')

print(sh.cell(1,3).value)
print(sh.cell(0,0).value)  #获取第一行第一列数据

print(sh.nrows)  #有多少行有效数据
print(sh.ncols)   #多少列有效数据

print(sh.row_values(0))  #第一行所有数据

for i in range(1,sh.nrows):
    data = sh.row_values(i)
    req = {
        'url':data[3],
        'method':data[4],
        'params': json.loads(data[5] or '{}'),
        'headers': json.loads(data[6] or'{}'),
        'data': json.loads(data[7] or '{}'),
        'json': json.loads(data[8] or '{}')
}
    #print(req)
    # res = requests.request(**req).json()
    #print(res.text)
    # print(res.json())
    ASSET =data[9].split('\n')
    print(ASSET)
    for expr in ASSET:
        print(expr)
        assert eval(expr)
