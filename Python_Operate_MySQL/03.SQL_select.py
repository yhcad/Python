#Python-实例演示select数据
import pymysql

# 打开数据库连接
conn = pymysql.connect("localhost","root","123456cdcC","student" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
sql = "select * from user"
cursor.execute(sql)

rs=cursor.fetchall()
#占位符%s
"""
rs表示的是数据库中的每个元组，其中，元组的概念是指数据库中每一行元素；for循环每次取rs的一个元组出来，
row元素里面包含有2个值，本别以string形式输出到userid 和username
"""

for row in rs:
    print("userid=%s,username=%s" %row)

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print ("Database version : %s " % data)

cursor.close()
# 关闭数据库连接
conn.close()


