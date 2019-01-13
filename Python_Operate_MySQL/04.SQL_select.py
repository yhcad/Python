#Python-实例演示select数据
import pymysql
 
# 打开数据库连接
conn = pymysql.connect("localhost","root","123456cdcC","student" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
sql = "select * from user"
cursor.execute(sql)
#打印本地获取的数据行数
print(cursor.rowcount)
#获取第一行记录
rs=cursor.fetchone()
print(rs)
#获取3行记录
rs=cursor.fetchmany(3)
print(rs)
#获取剩下的记录
rs=cursor.fetchall()
print(rs)

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print ("Database version : %s " % data)

cursor.close()
# 关闭数据库连接
conn.close()


