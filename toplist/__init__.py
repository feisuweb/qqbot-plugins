# -*- coding: utf-8 -*-

def onQQMessage(bot, contact, member, content):
	
    if content.find('谁能做')>0:
        bot.SendTo(contact, '你好，我是外包群管家，请问我能帮到您做什么？')
