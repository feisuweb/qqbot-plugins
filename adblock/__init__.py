# -*- coding: utf-8 -*-
def onQQMessage(bot, contact, member, content):
	if  '彩票'  in content:
		kickUser(bot, contact, member, content)
	if  '免费注册公司'  in content:
		kickUser(bot, contact, member, content)		
	if  '代理记账报税'  in content:
		kickUser(bot, contact, member, content)		
	if  '开正规发票'  in content:
		kickUser(bot, contact, member, content)		
	if  '真人娱乐'  in content:
		kickUser(bot, contact, member, content)
	if  '飞讯群发器' in content:
		kickUser(bot, contact, member, content)
	if  '群发器' in content:
		kickUser(bot, contact, member, content)		
	if  '进群' in content:
		kickUser(bot, contact, member, content)
	if  '免费观看' in content:
		kickUser(bot, contact, member, content)
	if  '色情群' in content:
		kickUser(bot, contact, member, content)		
	if  '欢迎加群' in content:
		kickUser(bot, contact, member, content)
	if  '网站 8222' in content:
		kickUser(bot, contact, member, content)
	if  '点击群号秒进' in content:
		kickUser(bot, contact, member, content)	
	#以下关键词会被禁言
	if  'http://' in content or 'https://' in content or '.cn' in content or '.com' in content:
		shutUser(bot, contact, member, content)
	if  'QQ：' in content:
		shutUser(bot, contact, member, content)
	if  'QQ:' in content:
		shutUser(bot, contact, member, content)
	if  '加我微信' in content:
		shutUser(bot, contact, member, content)
	if  '加微信' in content:
		shutUser(bot, contact, member, content)
	if  '加我QQ' in content:
		shutUser(bot, contact, member, content)
	if  '加我扣扣' in content:
		shutUser(bot, contact, member, content)
	if  '加扣扣' in content:
		shutUser(bot, contact, member, content)
	if  '加QQ' in content:
		shutUser(bot, contact, member, content)	
	if  '欢迎小窗口联系' in content:
		shutUser(bot, contact, member, content)			

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