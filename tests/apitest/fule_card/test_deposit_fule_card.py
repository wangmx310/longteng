
import requests
import pytest

from utils.db import LongTengServer
db = LongTengServer()
data = ['1#', '-10', '34q']


@pytest.mark.smoke
@pytest.mark.api
def test_deposit_fule_card0():
    print(f'测试加油卡充值:{19940310010}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '03A',
        'CardInfo': {
            'cardNumber': '19940310010',
            'cardBalance': '1'
        }
    }
    res = requests.post(url=url, json=data).json()
    # print(res.text)
    assert 200 == res['code']
    assert '充值成功' == res['msg']
    assert '1' == res['result']['cardBalance']
    assert '19940310010' == res['result']['cardNumber']
    assert 5010 == res['result']['cardStatus']
    assert 742325569 == res['result']['id']
    assert 11283 == res['result']['userId']
    assert res['success'] is True


@pytest.mark.smoke
@pytest.mark.api
def test_deposit_fule_card1():
    print(f'测试业务id不能为空:{19940310010}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': '',
        'methodId': '03A',
        'CardInfo': {
            'cardNumber': '19940310010',
            'cardBalance': '1'
        }
    }
    res = requests.post(url=url, json=data).json()
    # print(res.text)
    assert 301 == res['code']
    assert '业务ID不能为空!' == res['msg']
    assert res['success'] is True


@pytest.mark.smoke
@pytest.mark.api
def test_deposit_fule_card2():
    print(f'测试第三方平台ID不能为空!:{19940310010}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '',
        'CardInfo': {
            'cardNumber': '19940310010',
            'cardBalance': '1'
        }
    }
    res = requests.post(url=url, json=data).json()
    # print(res.text)
    assert 301 == res['code']
    assert '第三方平台ID不能为空!' == res['msg']
    assert res['success'] is False


@pytest.mark.smoke
@pytest.mark.api
def test_deposit_fule_card3():
    print(f'测试卡号不能为空!:{19940310010}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '03A',
        'CardInfo': {
            'cardNumber': '',
            'cardBalance': '1'
        }
    }
    res = requests.post(url=url, json=data).json()
    # print(res.text)
    assert 300 == res['code']
    assert '卡号不能为空!' == res['msg']
    assert res['success'] is False


@pytest.mark.smoke
@pytest.mark.api
def test_deposit_fule_card4():
    print(f'测试金额不能为空!:{19940310010}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '03A',
        'CardInfo': {
            'cardNumber': '19940310010',
            'cardBalance': ''
        }
    }
    res = requests.post(url=url, json=data).json()
    # print(res.text)
    assert 300 == res['code']
    assert '金额不能为空' == res['msg']
    assert res['success'] is False


@pytest.mark.smoke
@pytest.mark.api
def test_deposit_fule_card5():
    print(f'测试卡号不存在!:{19940310004}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '03A',
        'CardInfo': {
            'cardNumber': '19940310004',
            'cardBalance': '1'
        }
    }
    res = requests.post(url=url, json=data).json()
    # print(res.text)
    assert 5013 == res['code']
    assert '加油卡号不存在' == res['msg']
    assert res['success'] is False


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parametrize('card_balance', data)
def tes_deposit_fule_card6(card_balance,db):
    print(f'金额不正确:{card_balance}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '03A',
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