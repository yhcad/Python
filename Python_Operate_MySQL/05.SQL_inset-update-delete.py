 #Python-实例演示inset-update-delete数据 
import pymysql
 
# 打开数据库连接

conn = pymysql.connect("localhost","root","123456cdcC","student" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
#插入一条记录；
sql_insert="insert into user(userid,username) values(10,'name10')"
#修改一条记录
sql_update="update user set username='name91' where userid=9"
#删除记录
sql_delete="delete from user where userid<3"

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)
    
    conn.commit()
except Exception as e:
    #打印出错信息
    print(e)
    #事务回流
    conn.rollback()

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


