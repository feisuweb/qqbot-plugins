# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

def onQQMessage(bot, contact, member, content):
	if content.find('[@ME]') == -1:
		return True
	else:
		ai_chat(bot, contact, member, content)
		
def ai_chat(bot, contact, member, content):
	#防止机器人对聊
	try:
		paraf={ 'userid' : '1111', 'key' : 'ff395a1b69e2452f95fa47adaf80f95e', 'info' : content}
		info =http_post('http://www.tuling123.com/openapi/api',paraf)
		info = json.loads(info)
		if info["code"] in [40001, 40003, 40004]:
			 bot.SendTo(contact,"我今天累了，不聊了")
		elif info["code"] in [40002, 40005, 40006, 40007]:
			 bot.SendTo(contact,"我遇到了一点问题，请稍后@我,问题代码："+info["code"])
		else:
			 rpy = str(info["text"]).replace('<主人>','你').replace('<br>',"\n")
			 bot.SendTo(contact,rpy)
		return True
	except Exception, e:
		bot.SendTo(contact,str(e))
	return False		
	
	
def http_post(url,data):
    jdata = json.dumps(data)             # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata)       # 生成页面请求的完整数据
    response = urllib2.urlopen(req)       # 发送页面请求
    return response.read()                    # 获取服务器返回的页面信息