# -*- coding: utf-8 -*-
import pymysql  
import datetime
def onQQMessage(bot, contact, member, content):
	if  '彩票'  in content:
		kickUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'彩票')
	if  '需要请联系本Q'  in content:
		kickUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'需要请联系本Q')
	if  '免费注册公司'  in content:
		kickUser(bot, contact, member, content)		
		insertChatAdContent(bot,contact,member,content,'免费注册公司')
	if  '代理记账报税'  in content:
		kickUser(bot, contact, member, content)		
		insertChatAdContent(bot,contact,member,content,'代理记账报税')
	if  '开正规发票'  in content:
		kickUser(bot, contact, member, content)		
		insertChatAdContent(bot,contact,member,content,'开正规发票')
	if  '真人娱乐'  in content:
		kickUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'真人娱乐')
	if  '飞讯群发器' in content:
		kickUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'飞讯群发器')
	if  '群发器' in content:
		kickUser(bot, contact, member, content)		
		insertChatAdContent(bot,contact,member,content,'群发器')
	if  '进群' in content:
		kickUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'进群')
	if  '免费观看' in content:
		kickUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'免费观看')
	if  '色情群' in content:
		kickUser(bot, contact, member, content)		
		insertChatAdContent(bot,contact,member,content,'色情群')
	if  '欢迎加群' in content:
		kickUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'欢迎加群')
	if  '网站 8222' in content:
		kickUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'网站 8222')
	if  '点击群号秒进' in content:
		kickUser(bot, contact, member, content)	
		insertChatAdContent(bot,contact,member,content,'点击群号秒进')
	if  '双击群号' in content:
		kickUser(bot, contact, member, content)	
		insertChatAdContent(bot,contact,member,content,'双击群号')
	if  '点击群号' in content:
		kickUser(bot, contact, member, content)	
		insertChatAdContent(bot,contact,member,content,'点击群号')
		
	#以下关键词会被禁言
	if  'http://' in content or 'https://' in content or '.cn' in content or '.com' in content:
		shutUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'网址')
	if  '出售' in content:
		shutUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'网址')
	if  'QQ：' in content:
		shutUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'QQ：')
	if  'QQ:' in content:
		shutUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'QQ')
	if  '加我微信' in content:
		shutUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'加我微信')
	if  '加微信' in content:
		shutUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'加微信')
	if  '加我QQ' in content:
		shutUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'加我QQ')
	if  '加我扣扣' in content:
		shutUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'加我扣扣')
	if  '加扣扣' in content:
		shutUser(bot, contact, member, content)
		insertChatAdContent(bot,contact,member,content,'加扣扣')
	if  '加QQ' in content:
		shutUser(bot, contact, member, content)	
		insertChatAdContent(bot,contact,member,content,'加QQ')
	if  '欢迎小窗口联系' in content:
		shutUser(bot, contact, member, content)			
		insertChatAdContent(bot,contact,member,content,'欢迎小窗口联系')

#踢出用户出群		
def kickUser(bot, contact, member, content):
		gl = bot.List('group', contact.name)
		if gl:
			group = gl[0]
			membs = bot.List(group, member.name)
			if membs:
				bot.GroupKick(group, membs)
				bot.SendTo(contact, '用户'+member.name+'('+member.qq+')因在群里用群发器群发广告，已经被及时踢出群。发广告请走心，注意：禁止使用群发器发广告，违者踢出群。')
				bot.SendTo(contact, '本群严格禁止用群发器群发小广告，刷屏，以及小号加群（QQ年龄小于5，请用QQ年龄大于等于5的号加群）的行为，发广告请走心，注意：禁止使用群发器发广告，违者立即踢出群。')

#禁言用户
def shutUser(bot, contact, member, content):
		gl = bot.List('group', contact.name)
		if gl:
			group = gl[0]
			membs = bot.List(group, member.name)
			if membs:
				bot.GroupShut(group, membs,86400)				
				bot.SendTo(contact, '用户'+member.name+'('+member.qq+')因在群里发疑似广告内容，已经被禁言24个小时，重复多次，将会被踢出群。如被误禁言，请找群主处理。')

def insertChatAdContent(bot,contact,member,content,keyword):
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
	sql = "INSERT INTO chat_ads (group_number,group_name,qq,nickname,mark,content,create_time,keyword) VALUES ( '%s', '%s', '%s','%s','%s', '%s', '%s','%s')"  
	name = pymysql.escape_string(contact.name)
	nickname = pymysql.escape_string(member.name)
	mark = pymysql.escape_string(member.name)
	data = (contact.qq,name,member.qq,nickname,mark,content,createtime,keyword)  
	cursor.execute(sql % data)  
	connect.commit()  
	print('insert ad success', cursor.rowcount, ' record') 