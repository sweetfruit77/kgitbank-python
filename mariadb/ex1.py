# cos DB연결
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='qwer1324', db='test', charset='utf8')
# 커서 만들기
cursor = db.cursor()

sql = """
    drop table if exists baseball;
"""
cursor.execute(sql)

sql = """
    create table baseball(
        id int,
        name varchar(20)
    );
"""
cursor.execute(sql)

cursor.execute("show tables")
db.commit()

