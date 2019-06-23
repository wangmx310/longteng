
import pytest

from utils.db import LongTengServer


@pytest.fixture(scope='session')
def db():
    db = LongTengServer()   #建立数据库连接
    yield db
    db.close()  #关闭数据库
