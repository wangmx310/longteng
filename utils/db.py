import pymysql
import os
DB_CONF = {
    # 'host': os.getenv('MYSQL_HOST'),
    # 'port': int(os.getenv('MYSQL_PORT')),
    # 'db': os.getenv('MYSQL_DB'),
    # 'user': os.getenv('MYSQL_USER'),
    # 'password': os.getenv('MYSQL_PWD'),
    # 'autocommit': True,
    # 'charset': 'utf8'
    'host': '115.28.108.130',
    'port': 3306,
    'db': 'longtengserver',
    'user': 'test',
    'password': '123456',
    'autocommit': True,  # 每执行一条sql自动提交
    'charset': 'utf8'
}


class DB(object):
    def __init__(self):
        print('建立数据库连接')
        self.conn = pymysql.connect(**DB_CONF)
        self.cur = self.conn.cursor()    #建立游标，从缓冲区拿数据

    def execute(self, sq1):
        print(f'执行sql:{sq1}')
        self.cur.execute(sq1)
        result = self.cur.fetchall()
        print(f'执行结果:{result}')
        return result

    def close(self):
        print('关闭数据库连接')
        self.conn.close()

if __name__ == '__main__':              #一般用来调试当前模块，是有从当前模块运行时才执行
    db=DB()
    r=db.execute('select id from cardinfo where cardNumbr="123456"')
    print(r)
    db.close()

class LongTengServer(DB):
    """该项目数据库的常用业务操作封装"""
    def del_card(self,card_number):
        print(f'数据库删除加油卡:{card_number}')
        sql = f'delete from cardinfo where cardNumber="{card_number}"'
        self.execute(sql)

    def del_card(self,card_number):
        print(f'数据库查询加油卡:{card_number}')
        sql = f'select cardNumber from cardinfo where cardNumber="{card_number}"'
        result = self.execute(sq1)
        # if result !=():
        #     return True
        # else:
        #     return False
        return True if result else False   #如果result为真（非（）），返回True，否则返回False
        self.execute(sql)

