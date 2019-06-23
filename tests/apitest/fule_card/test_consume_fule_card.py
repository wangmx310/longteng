
import requests
import pytest

from utils.db import LongTengServer
db = LongTengServer()
data = ['1#', '-10', '34q']

@pytest.mark.smoke
@pytest.mark.api
def tes_consume_fule_card0():
    print(f'测试消费加油卡:{19940310010}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '04A',
        'CardUser':{
            'userId':'11283'
        },
        'CardInfo': {
            'cardNumber': '19940310010',
            'cardBalance': '1'
        }
    }
    res = requests.post(url=url, json=data).json()
    print(res.text)
    assert 200 == res['code']
    assert '消费成功!' == res['msg']
    assert res['success'] is True


@pytest.mark.smoke
@pytest.mark.api
def tes_consume_fule_card1():
    print(f'测试消费大于余额:{19940310010}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '04A',
        'CardUser': {
            'userId': '11283'
        },
        'CardInfo': {
            'cardNumber': '19940310010',
            'cardBalance': '1000000'
        }
    }
    res = requests.post(url=url, json=data).json()
    print(res.text)
    assert 200 == res['code']
    assert '对不起，您的余额不足，请充值!' == res['msg']
    assert res['success'] is False


@pytest.mark.smoke
@pytest.mark.api
def tes_consume_fule_card2():
    print(f'测试卡号不存在:{19940310004}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '04A',
        'CardUser': {
            'userId': '11283'
        },
        'CardInfo': {
            'cardNumber': '19940310004',
            'cardBalance': '1'
        }
    }
    res = requests.post(url=url, json=data).json()
    print(res.text)
    assert 5013 == res['code']
    assert '根据用户ID没有查询到卡号!' == res['msg']
    assert res['success'] is False


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parametrize('card_balance', data)
def tes_consume_fule_card3(card_balance,db):
    print(f'金额不正确:{card_balance}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '04A',
        'CardUser': {
            'userId': '11283'
        },
        'CardInfo': {
            'cardNumber': '19940310010',
            'cardBalance': 'card_balance'
        }
    }
    res = requests.post(url=url, json=data).json()
    print(res.text)
    assert 300 == res['code']
    assert '金额不正确!' == res['msg']
    assert res['success'] is False


@pytest.mark.smoke
@pytest.mark.api
def tes_consume_fule_card2():
    print(f'测试userid不存在:{19940310004}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '04A',
        'CardUser': {
            'userId': '1128009'
        },
        'CardInfo': {
            'cardNumber': '19940310004',
            'cardBalance': '1'
        }
    }
    res = requests.post(url=url, json=data).json()
    print(res.text)
    assert 5013 == res['code']
    assert '根据用户ID没有查询到卡号!' == res['msg']
    assert res['success'] is False