
import requests
import pytest

from utils.data import get_data

DATA = get_data

data = ['1994031001', 'abcqwe', '123abc', '3848#wdd', '添加卡号', '']
data1 = ['19940310', '19940310001', '1994031002','19940310003', '19940310005']

@pytest.mark.smoke
@pytest.mark.parametrize('card_number', data)
#@pytest.mark.skipif(db.check_card('1234556'),'卡号已存在')  #环境检查
def test_add_fule_card0(card_number, db):
    print(f'测试添加加油卡:{card_number}')
    db.del_card(card_number)
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {'dataSourceId': 'bHRz', 'methodId': '00A', 'CardInfo': {'cardNumber': card_number}}
    res = requests.post(url, json=data).json()
    print(f'响应报文:{res}')
    assert 200 == res['code']
    assert '添加卡成功' == res['msg']
    assert res['success'] is False
    assert db.check_card('card_number') is True   #数据库断言
    db.del_card(card_number)


@pytest.mark.smoke
@pytest.mark.parametrize('card_number', data1)
#@pytest.mark.skipif(db.check_card('card_number'), '卡号已存在')  #环境检查
def test_add_fule_card1(card_number, db):
    print(f'测试添加加油卡:{card_number}')
    db.del_card(19940310)
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {'dataSourceId': 'bHRz', 'methodId': '00A', 'CardInfo': {'cardNumber': card_number}}
    res = requests.post(url, json=data).json()
    print(f'响应报文:{res}')
    assert 200 == res['code']
    assert '添加卡成功' == res['msg']
    assert res['success'] is False
    assert db.check_card('card_number') is True   #数据库断言


@pytest.mark.smoke
@pytest.mark.api
def test_add_fule_card2(db):
    print(f'测试重复添加加油卡:{2019053002}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '00A',
        'CardInfo': {
            'cardNumber': '2019053002'
        }
    }
    res = requests.post(url=url, json=data).json()
    print(f'响应报文:{res}')
    assert 5000 == res['code']
    assert '该卡已添加' == res['msg']
    assert False == res['success']
    assert db.check_card('card_number') is False


@pytest.mark.smoke
@pytest.mark.api
def test_add_fule_card3(db):
    print(f'测试入参不正确:{2019053002001}')
    db.del_card(2019053002001)
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': '',
        'methodId': '00A',
        'CardInfo': {
            'cardNumber': '2019053002001'
        }
    }
    res = requests.post(url=url, json=data).json()
    print(f'响应报文:{res}')
    assert 301 == res['code']
    assert '第三方平台ID不能为空!' == res['msg']
    assert False == res['success']
    assert db.check_card('card_number') is False
    db.del_card(2019053002001)


@pytest.mark.smoke
@pytest.mark.api
def test_add_fule_card4(db):
    print(f'测试入参不正确:{2019053002001}')
    db.del_card(2019053002001)
    url='http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '',
        'CardInfo': {
            'cardNumber': '2019053002001'
        }
    }
    res = requests.post(url=url, json=data).json()
    print(f'响应报文:{res}')
    assert 301 == res['code']
    assert '业务ID不能为空!' == res['msg']
    assert False == res['success']
    assert db.check_card('card_number') is False
    db.del_card(2019053002001)

