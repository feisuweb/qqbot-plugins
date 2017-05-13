# -*- coding: utf-8 -*-

def onQQMessage(bot, contact, member, content):
	
    if '谁能做' in content:
		bot.SendTo(contact, '@'+member.name+'您好，请问需求是什么？详细的私聊。')
		
    if '[@ME]' in content:
        bot.SendTo(contact, '@'+member.name+' 您好，请问我能帮到您做什么？')
