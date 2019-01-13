 #Python操作MySQL银行转账实例-代码流程
 # coding:utf8
import pymysql
import sys
class TransferMoney(object):
    def __init__(self,conn):
        self.conn=conn
        #检查帐号是否可用 
    def check_acct_available(self,acctid):
        cursor = self.conn.cursor() 
        try:
            sql = "select * from account where acctid=%s" %acctid
            cursor.execute(sql)
            print("check_acct_available:" + sql)
            rs = cursor.fetchall()
            if len(rs)!=1:
                raise Exception("帐号%s不存在" %acctid)
        finally:
            cursor.close()
    #检查帐号是否有足够的钱
    def has_enough_money(self,acctid,money):
        cursor = self.conn.cursor() 
        try:
            sql = "select * from account where acctid=%s and money>%s" %(acctid,money)
            cursor.execute(sql)
            print("has_enough_money:" + sql)
            rs = cursor.fetchall()
            if len(rs)!=1:
                raise Exception("帐号%s没有足够的钱" %acctid)
        finally:
            cursor.close()
   #检查帐号减款
    def reduce_money(self,acctid,money):
        cursor = self.conn.cursor() 
        try:
            sql = "update account set money=money-%s where acctid =%s" %(money,acctid)
            cursor.execute(sql)
            print("reduce_money:" + sql)
            if  cursor.rowcount != 1:
                raise Exception("帐号%s减款失败"  %acctid)
        finally:
            cursor.close()
     #检查帐号加款      
    def add_money(self,acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid =%s" %(money,acctid)
            cursor.execute(sql)
            print("add_money:" + sql)
            if cursor.rowcount != 1:
                raise Exception("帐号%s加款失败"  %acctid)
        finally:
            cursor.close()  
        
    def transfer(self,source_acctid,target_acctid,money):
        try:
            #检查收款人和收款人帐号是否可用 
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            #检查是否有足够的钱 
            self.has_enough_money(source_acctid,money)
            self.reduce_money(source_acctid,money)
            self.add_money(target_acctid,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
            
if __name__ == "__main__":
    #付款人账号
    source_acctid = sys.argv[1]
    #收款人账号
    target_acctid = sys.argv[2]
    #转账金额
    money =sys.argv[3]
    
    # 打开数据库连接
    conn = pymysql.connect("localhost","root","123456cdcC","student" )
    #创建对象，使用TransferMoney类操作
    tr_money =TransferMoney(conn)
    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print("出现问题：" + str(e))
    finally:  
        conn.close()



