
import requests
import pytest

from utils.db import LongTengServer
db = LongTengServer()

@pytest.mark.smoke
@pytest.mark.api
def test_bind_fule_card0():
    print(f'测试绑定加油卡:{19940310}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data={
        'dataSourceId': 'bHRz',
        'methodId': '01A',
        'CardUser': {
            'userName': '小九',
            'idType': '1',
            'idNumber': '1109999008766110',
            'email': '15096484888@qq.com',
            'gender': '1'
        },
        'CardInfo': {
            'cardNumber': '19940310'
        }
    }
    res = requests.post(url=url,json=data).json()
    #print(res.text)
    assert 5010 == res['code']
    assert '绑定成功' == res['msg']
    assert res['success'] is True
    db.del_card(19940310)


@pytest.mark.smoke
@pytest.mark.api
def test_bind_fule_card1():
    print(f'测试重复绑定加油卡:{19940310001}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data={
        'dataSourceId': 'bHRz',
        'methodId': '01A',
        'CardUser': {
            'userName': '小九',
            'idType': '1',
            'idNumber': '1109999008766110',
            'email': '15096484888@qq.com',
            'gender': '1'
        },
        'CardInfo': {
            'cardNumber': '19940310001'
        }
    }
    res = requests.post(url=url,json=data).json()
    #print(res.text)
    assert 5010 == res['code']
    assert '绑定成功' == res['msg']
    assert res['success'] is True
    db.del_card(19940310001)


@pytest.mark.smoke
@pytest.mark.api
def test_bind_fule_card2():
    print(f'测试最多绑定两张卡:{19940310002}')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data={
        'dataSourceId': 'bHRz',
        'methodId': '01A',
        'CardUser': {
            'userName': '小九',
            'idType': '1',
            'idNumber': '1109999008766110',
            'email': '15096484888@qq.com',
            'gender': '1'
        },
        'CardInfo': {
            'cardNumber': '19940310002'
        }
    }
    res = requests.post(url=url,json=data).json()
    #print(res.text)
    assert 5014 == res['code']
    assert '每个用户只能绑定两张卡' == res['msg']
    assert res['success'] is False
    db.del_card(19940310002)


@pytest.mark.smoke
@pytest.mark.api
def test_bind_fule_card3():
    print(f'测试卡号不存在:{19940310004}')
    db.del_card(19940310009)
    url = 'http://115.28.108.130:8080/gasStation/process'
    data={
        'dataSourceId': 'bHRz',
        'methodId': '01A',
        'CardUser': {
            'userName': '小九',
            'idType': '1',
            'idNumber': '1109999008766110',
            'email': '15096484888@qq.com',
            'gender': '1'
        },
        'CardInfo': {
            'cardNumber': '19940310004'
        }
    }
    res = requests.post(url=url,json=data).json()
    #print(res.text)
    assert 5010 == res['code']
    assert '绑定成功' == res['msg']
    assert res['success'] is True
    db.del_card(19940310004)


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.skipif(db.check_card('19940310005'),'卡号已存在')
def test_bind_fule_card4():
    print(f'测试methonid无效:{19940310005}')
    db.del_card(19940310002)
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '05A',
        'CardUser': {
            'userName': '小九',
            'idType': '1',
            'idNumber': '1109999008766110',
            'email': '15096484888@qq.com',
            'gender': '1'
        },
        'CardInfo': {
            'cardNumber': '19940310005'
        }
    }
    res = requests.post(url=url, json=data).json()
    # print(res.text)
    assert 199 == res['code']
    assert '业务ID无效' == res['msg']
    assert res['success'] is False
    db.del_card(19940310005)


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.skipif(db.check_card('19940310003'),'卡号已存在')
def test_bind_fule_card5():
    print(f'测试卡号是黑名单:{19940310003}')
    db.execute('UPDATE cardinfo set cardstatus=5011 WHERE cardNumber=19940310003')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '05A',
        'CardUser': {
            'userName': '小九',
            'idType': '1',
            'idNumber': '1109999008766110',
            'email': '15096484888@qq.com',
            'gender': '1'
        },
        'CardInfo': {
            'cardNumber': '19940310003'
        }
    }
    res = requests.post(url=url, json=data).json()
    # print(res.text)
    assert 5011 == res['code']
    assert '卡号是否黑名单,无法绑定' == res['msg']
    assert res['success'] is False

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.skipif(db.check_card('19940310003'), '卡号已存在')
def test_bind_fule_card6():
    print(f'测试卡号已注销:{19940310003}')
    db.execute('UPDATE cardinfo set cardstatus=5012 WHERE cardNumber=19940310003')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '05A',
        'CardUser': {
            'userName': '小九',
            'idType': '1',
            'idNumber': '1109999008766110',
            'email': '15096484888@qq.com',
            'gender': '1'
        },
        'CardInfo': {
            'cardNumber': '19940310003'
        }
    }
    res = requests.post(url=url, json=data).json()
    # print(res.text)
    assert 5012 == res['code']
    assert '卡号已经注销,无法绑定' == res['msg']
    assert res['success'] is False


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.skipif(db.check_card('19940310003'), '卡号已存在')
def test_bind_fule_card7():
    print(f'测试单位卡:{19940310003}')
    db.execute('UPDATE cardinfo set cardstatus=5021 WHERE cardNumber=19940310003')
    url = 'http://115.28.108.130:8080/gasStation/process'
    data = {
        'dataSourceId': 'bHRz',
        'methodId': '05A',
        'CardUser': {
            'userName': '小九',
            'idType': '1',
            'idNumber': '1109999008766110',
            'email': '15096484888@qq.com',
            'gender': '1'
        },
        'CardInfo': {
            'cardNumber': '19940310003'
        }
    }
    res = requests.post(url=url, json=data).json()
    # print(res.text)
    assert 5021 == res['code']
    assert '单位卡不支持,无法绑定' == res['msg']
    assert res['success'] is False