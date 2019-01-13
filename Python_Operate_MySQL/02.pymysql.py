#电脑终端使用pip install pymysql 安装pymysql
import pymysql
# 打开数据库连接
#连接数据库的用户名为 "root"，密码为"123456cdcC",Mysql数据库用户授权请使用Grant命令。
db = pymysql.connect("localhost","root","123456cdcC","student" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()


