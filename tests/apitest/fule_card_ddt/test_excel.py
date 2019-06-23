import os
import json

import requests
import pytest
from utils.path import DATA_DIR
from utils.data import Excel

data_file = os.path.join(DATA_DIR, 'data.xls')


def json2dict(text):      #json字符串转字典
    # if text =='':
    #     text = '{}'
    text = text or'{}'    #如果text为空,取{}
    try:
       return json.loads(text)
    except json.decoder.JSONDecodeError:
        pytest(f'{text}不是合法的json格式')


def test_fule_card(db):
    excel =Excel(data_file)
    data = excel.get_sheet('执行用例')
    case = data[0]
    print(case)
    print(f"执行用例：编号：{case['SN']}模块:{case['MODULE']}标题:{case['TITLE']}")
    #组装请求
    print(f'发送请求.....')
    setups = case['SETUP']
    if setups:            #如果setups不为空
        for line in setups.split('\n'):   #将setups按换行符分割
            eval(line.strip)
            assert print(line.strip(), {}, {'db': db})


    res=requests.request(
        method=case['METHOD'],
        url=case['URL'],
        params=json2dict(case['PARAMS']),
        headers=json2dict(case['HEADERS']),
        data=json2dict(case['DATA']),
        json=json2dict(case['JSON'])
    ).json()

    ass = case['ASSERT']
    if ass:
        for line in ass.split('\n'):
            print(f'执行断言语句:{line.strip()}')
            assert eval(line.strip(), {}, {'db': db, 'res': res})

    teardowns = case['TEARDOWN']
    if teardowns:
        for line in teardowns.split('\n'):
            print(f'执行teardown语句:{line.strip()}')
            assert eval(line.strip(), {}, {'db': db, 'res': res})
    print(res)
