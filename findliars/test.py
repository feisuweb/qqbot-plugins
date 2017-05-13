#encoding:utf-8  
import pymysql  
# 连接数据库  
connect = pymysql.Connect(  
	host='localhost',  
	port=3306,  
	user='root',  
	passwd='root',  
	db='it_work_db',  
	charset='utf8'  
)  
  
# 获取游标  
cursor = connect.cursor()  
  
# 插入数据  
sql = "INSERT INTO users (qq, uin , nickname) VALUES ( '%s', '%s', %s )"  
data = ('test', '13512345678', '11')  
cursor.execute(sql % data)  
connect.commit()  
print('成功插入', cursor.rowcount, '条数据')  
  
# 修改数据  
#sql = "UPDATE users SET saving = %.2f WHERE account = '%s' "  
#data = (8888, '13512345678')  
#cursor.execute(sql % data)  
#connect.commit()  
#print('成功修改', cursor.rowcount, '条数据')  
  
# 查询数据  
#sql = "SELECT name,saving FROM users WHERE account = '%s' "  
#data = ('13512345678',)  
#cursor.execute(sql % data)  
#for row in cursor.fetchall():  
#    print("Name:%s\tSaving:%.2f" % row)  
#print('共查找出', cursor.rowcount, '条数据')  
  
# 删除数据  
#sql = "DELETE FROM users  WHERE account = '%s' LIMIT %d"  
#data = ('13512345678', 1)  
#cursor.execute(sql % data)  
#connect.commit()  
#print('成功删除', cursor.rowcount, '条数据')  
  
# 事务处理  
#sql_1 = "UPDATE users SET saving = saving + 1000 WHERE account = '18012345678' "  
#sql_2 = "UPDATE users SET expend = expend + 1000 WHERE account = '18012345678' "  
#sql_3 = "UPDATE users SET income = income + 2000 WHERE account = '18012345678' "  
  
#try:  
#    cursor.execute(sql_1)  # 储蓄增加1000  
#    cursor.execute(sql_2)  # 支出增加1000  
#    cursor.execute(sql_3)  # 收入增加2000  
#except Exception as e:  
#    connect.rollback()  # 事务回滚  
#    print('事务处理失败', e)  
#else:  
#    connect.commit()  # 事务提交  
#    print('事务处理成功', cursor.rowcount)  
  
# 关闭连接  
cursor.close()  
connect.close()  