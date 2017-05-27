# -*- coding: utf-8 -*-
import pymysql  
import datetime
def onQQMessage(bot, contact, member, content):
    if '招聘' in content:
        insertRecruitmentContent(bot,contact,member,content,'招聘')
        return
        
    if '招' in content and '诚招代理' not in content and '代理' not in content and '中招' not in content:
        insertRecruitmentContent(bot,contact,member,content,'招')		
        return

def insertRecruitmentContent(bot,contact,member,content,keyword):
	# 连接数据库  
	connect = pymysql.Connect(  
		host='localhost',  
		port=3306,  
		user='root',  
		passwd='mysql',  
		db='it_work_db',  
		charset='utf8'  
	)  
	  
	# 获取游标  
	cursor = connect.cursor()  
	now = datetime.datetime.now()
	createtime=now.strftime('%Y-%m-%d %H:%M:%S')  
	# 插入数据  
	sql = "INSERT INTO chat_recruitments (group_number,group_name,qq,nickname,mark,content,create_time,keyword) VALUES ( '%s', '%s', '%s','%s','%s', '%s', '%s','%s')"  
	name = pymysql.escape_string(contact.name)
	nickname = pymysql.escape_string(member.name)
	mark = pymysql.escape_string(member.name)
	data = (contact.qq,name,member.qq,nickname,mark,content,createtime,keyword)  
	cursor.execute(sql % data)  
	connect.commit()  
	print('insert recruitment success', cursor.rowcount, ' record') 
	
