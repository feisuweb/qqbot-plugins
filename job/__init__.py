# -*- coding: utf-8 -*-
import pymysql  
import datetime
def onQQMessage(bot, contact, member, content):
	if '求教' in content:
		insertJobContent(bot,contact,member,content,'求教')
		return
	if '付费求教' in content:
		insertJobContent(bot,contact,member,content,'付费求教')
		return
	if '会的私聊' in content:
		insertJobContent(bot,contact,member,content,'会的私聊')
		return
	if '谁会' in content:
		insertJobContent(bot,contact,member,content,'谁会')
		return
	if '有会' in content:
		insertJobContent(bot,contact,member,content,'有会')
		return		
	if '谁能做' in content:
		insertJobContent(bot,contact,member,content,'谁能做')
		return
		
	if '需要' in content and '谁需要' not in content and '需要的' not in content:
		insertJobContent(bot,contact,member,content,'需要')
		return
		
	if '做过' in content:
		insertJobContent(bot,contact,member,content,'做过')
		return
		
	if '制作' in content:
		insertJobContent(bot,contact,member,content,'制作')
		return
		
	if '求助' in content:
		insertJobContent(bot,contact,member,content,'求助')
		return	
		
	if '请高人指点' in content:
		insertJobContent(bot,contact,member,content,'请高人指点')
		return
		
	if '请问' in content:
		insertJobContent(bot,contact,member,content,'请问')
		return
		
	if '如何' in content:
		insertJobContent(bot,contact,member,content,'如何')
		return
		
	if '找' in content:
		insertJobContent(bot,contact,member,content,'找')
		return
		
	if '有偿' in content:
		insertJobContent(bot,contact,member,content,'有偿')
		return
	if '帮忙' in content:
		insertJobContent(bot,contact,member,content,'帮忙')
		return
	if '付费' in content:
		insertJobContent(bot,contact,member,content,'付费')
		return		
	if '[@ME]' in content:
		insertJobContent(bot,contact,member,content,'@我')	
		bot.SendTo(contact, '@'+member.name+' 您好，请问我能帮到您做什么？')
		return
		

def insertJobContent(bot,contact,member,content,keyword):
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
	now = datetime.datetime.now()
	createtime=now.strftime('%Y-%m-%d %H:%M:%S')  
	# 插入数据  
	sql = "INSERT INTO chat_jobs (group_number,group_name,qq,nickname,mark,content,create_time,keyword) VALUES ( '%s', '%s', '%s','%s','%s', '%s', '%s','%s')"  
	name = pymysql.escape_string(contact.name)
	nickname = pymysql.escape_string(member.name)
	mark = pymysql.escape_string(member.name)
	data = (contact.qq,name,member.qq,nickname,mark,content,createtime,keyword)  
	cursor.execute(sql % data)  
	connect.commit()  
	print('insert job success', cursor.rowcount, ' record') 
    #将记录转发到外包群
    
