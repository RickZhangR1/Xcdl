import pymssql
from Xcdl.settings import SQL_DATABASE,SQL_SERVER,SQL_PASSWORD,SQL_USER
conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER,  password=SQL_PASSWORD,database=SQL_DATABASE,charset='utf8')  #获取连接
cur=conn.cursor()#获取光标
class MsSql():
    @classmethod
    def insert_db_xcdl(cls,results):
        sqllang='''INSERT INTO dbo.tb_xcdl(proxy_country,proxy_ip,proxy_port,proxy_server_address,proxy_anonymous,proxy_type,proxy_survival_time,proxy_verify_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''
        try:
            cur.execute(sqllang,results)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
    @classmethod
    def select_name(self,ip):
        sql="select isnull((select top(1) 1 from tb_xcdl where proxy_ip=%s), 0)"
        cur.execute(sql,ip)
        return cur.fetchall()[0][0]
# result=MsSql.select_name('2')
# print(result)

