
import requests
import pytest

from utils.db import LongTengServer
db = LongTengServer()


@pytest.mark.smoke
@pytest.mark.api
def test_query_fule_card0():
    print(f'测试查询卡号:{19940310010}')
    url = 'http://115.28.108.130:8080/gasStation/process?dataSourceId=bHRz&userId=11283&cardNumber=19940310010&methodId=02A'
    res = requests.get(url=url)
    res_dict = res.json()
    print(res.text)
    assert 200 == res_dict['code']
    assert '成功返回' == res_dict['msg']
    assert '200' == res_dict['result']['cardBalance']
    assert '19940310010' == res_dict['result']['cardNumber']
    assert '已经被绑定,正常使用中' == res_dict['result']['cardStatus']
    assert '消费金额:50,时间:2019-05-31 23:23:52' == res_dict['result']['consumptionDetails'][0]
    assert '充值金额:100,时间:2019-05-31 23:04:27' == res_dict['result']['rechargeDetails'][0]
    assert '2019053002' == res_dict['result']['cardNumber']
    assert res['success'] is True


@pytest.mark.smoke
@pytest.mark.api
def test_query_fule_card1():
    print(f'测试用户不存在:{19940310004}')
    url = 'http://115.28.108.130:8080/gasStation/process?dataSourceId=bHRz&userId=10164&cardNumber=19940310004&methodId=02A'
    res = requests.get(url=url)
    res_dict = res.json()
    print(res.text)
    assert 400 == res_dict['code']
    assert '无查询信息' == res_dict['msg']
    assert res['success'] is False


@pytest.mark.smoke
@pytest.mark.api
def test_query_fule_card2():
    print(f'测试业务id不存在:{19940310004}')
    url = 'http://115.28.108.130:8080/gasStation/process?dataSourceId=bHRz&userId=11283&cardNumber=19940310010&methodId=05A'
    res = requests.get(url=url)
    res_dict = res.json()
    print(res.text)
    assert 400 == res_dict['code']
    assert '无查询信息' == res_dict['msg']
    assert res['success'] is False