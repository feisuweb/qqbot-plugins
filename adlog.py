# -*- coding: utf-8 -*-
import pymysql  
import datetime

# 如果不希望加载本插件，可以在配置文件中的 plugins 选项中删除 qqbot.plugins.chatlog 
from qqbot.utf8logger import DEBUG

def onInit(bot):
    # 初始化时被调用
    # 注意 : 此时 bot 尚未启动，因此请勿在本函数中调用 bot.List/SendTo/GroupXXX/Stop/Restart 等接口
    #       只可以访问配置信息 bot.conf
    # bot : QQBot 对象
    DEBUG('ON-INIT : qqbot.plugins.sampleslots')

def onQrcode(bot, pngPath, pngContent):
    # 获取到二维码时被调用
    # 注意 : 此时 bot 尚未启动，因此请勿在本函数中调用 bot.List/SendTo/GroupXXX/Stop/Restart 等接口
    #       只可以访问配置信息 bot.conf
    # bot : QQBot 对象
    # pngPath : 二维码图片路径
    # pngContent : 二维码图片内容
    DEBUG('ON-QRCODE: %s (%d bytes)', pngPath, len(pngContent))

def onQQMessage(bot, contact, member, content):
    # 当收到 QQ 消息时被调用
    # bot     : QQBot 对象，提供 List/SendTo/GroupXXX/Stop/Restart 等接口，详见文档第五节
    # contact : QContact 对象，消息的发送者
    # member  : QContact 对象，仅当本消息为 群或讨论组 消息时有效，代表实际发消息的成员
    # content : str 对象，消息内容
    if contact.ctype == 'group':
        if  '麻将'  in content:
            insertChatAdContent(bot,contact,member,content,'麻将')
            return
        if  '蓝鲸'  in content:
			insertChatAdContent(bot,contact,member,content,'蓝鲸')
			return
        if  '找我'  in content:
            insertChatAdContent(bot,contact,member,content,'找我')
            return
        if  '优惠'  in content:
            insertChatAdContent(bot,contact,member,content,'优惠')
            return
        if  '要的加我'  in content:
            insertChatAdContent(bot,contact,member,content,'要的加我')    
            return
        if  '/色  /色  /色'  in content:
            insertChatAdContent(bot,contact,member,content,'/色  /色  /色')    
            return
        if  '加我'  in content:
            insertChatAdContent(bot,contact,member,content,'加我')        
            return
        if  '私聊'  in content:
            insertChatAdContent(bot,contact,member,content,'私聊')
            return
        if  '可联系我'  in content:
            insertChatAdContent(bot,contact,member,content,'可联系我')
            return
        if  '需要请联系本Q'  in content:
            insertChatAdContent(bot,contact,member,content,'需要请联系本Q')
            return
        if  '微信'  in content:
            insertChatAdContent(bot,contact,member,content,'微信')        
            return
        if  '要的私聊'  in content:
            insertChatAdContent(bot,contact,member,content,'要的私聊')        
            return
        if  '彩票'  in content:
            insertChatAdContent(bot,contact,member,content,'彩票')
            return
        if  '注册公司'  in content:
            insertChatAdContent(bot,contact,member,content,'注册公司')
            return        
        if  '代理记账'  in content:
            insertChatAdContent(bot,contact,member,content,'代理记账')
            return        
        if  '记账报税'  in content:
            insertChatAdContent(bot,contact,member,content,'记账报税')
            return                
        if  '商标注册'  in content:
            insertChatAdContent(bot,contact,member,content,'商标注册')
            return                
        if  '注册亚马逊'  in content:
            insertChatAdContent(bot,contact,member,content,'注册亚马逊')
            return
        if  '注册香港公司'  in content:
            insertChatAdContent(bot,contact,member,content,'注册香港公司')
            return                
        if  '免费注册公司'  in content:
            insertChatAdContent(bot,contact,member,content,'免费注册公司')
            return
        if  '代理记账报税'  in content:    
            insertChatAdContent(bot,contact,member,content,'代理记账报税')
            return
        if  '开正规发票'  in content:
            insertChatAdContent(bot,contact,member,content,'开正规发票')
            return
        if  '真人娱乐'  in content:
            insertChatAdContent(bot,contact,member,content,'真人娱乐')
            return
        if  '飞讯群发器' in content:
            insertChatAdContent(bot,contact,member,content,'飞讯群发器')
            return
        if  '群发器' in content:
            insertChatAdContent(bot,contact,member,content,'群发器')
            return
        if  '进群' in content:
            insertChatAdContent(bot,contact,member,content,'进群')
            return
        if  '免费观看' in content:
            insertChatAdContent(bot,contact,member,content,'免费观看')
            return
        if  '色情群' in content:
            insertChatAdContent(bot,contact,member,content,'色情群')
            return
        if  '欢迎加群' in content:
            insertChatAdContent(bot,contact,member,content,'欢迎加群')
            return
        if  '网站 8222' in content:
            insertChatAdContent(bot,contact,member,content,'网站 8222')
            return
        if  '点击群号秒进' in content:
            insertChatAdContent(bot,contact,member,content,'点击群号秒进')
            return
        if  '双击群号' in content:
            insertChatAdContent(bot,contact,member,content,'双击群号')
            return
        if  '点击群号' in content:
            insertChatAdContent(bot,contact,member,content,'点击群号')
            return
        if  '出售' in content:
            insertChatAdContent(bot,contact,member,content,'出售')        
            return
        if  '订购热线'  in content:
            insertChatAdContent(bot,contact,member,content,'订购热线')
            return
        if  'http://' in content or 'https://' in content or '.cn' in content or '.com' in content:
            insertChatAdContent(bot,contact,member,content,'网址')
            return
        if  'QQ：' in content:
            insertChatAdContent(bot,contact,member,content,'QQ：')
            return
        if  'QQ:' in content:
            insertChatAdContent(bot,contact,member,content,'QQ')
            return
        if  '加我微信' in content:
            insertChatAdContent(bot,contact,member,content,'加我微信')
            return
        if  '加微信' in content:
            insertChatAdContent(bot,contact,member,content,'加微信')
            return
        if  '加我QQ' in content:
            insertChatAdContent(bot,contact,member,content,'加我QQ')
            return
        if  '加我扣扣' in content:
            insertChatAdContent(bot,contact,member,content,'加我扣扣')
            return
        if  '加扣扣' in content:
            insertChatAdContent(bot,contact,member,content,'加扣扣')
            return
        if  '加QQ' in content:
            insertChatAdContent(bot,contact,member,content,'加QQ')
            return
        if  '欢迎小窗口联系' in content:
            insertChatAdContent(bot,contact,member,content,'欢迎小窗口联系')
            return

def onInterval(bot):
    # 每隔 5 分钟被调用
    # bot : QQBot 对象，提供 List/SendTo/GroupXXX/Stop/Restart 等接口，详见文档第五节
    DEBUG('INTERVAL')

def onStartupComplete(bot):
    # 启动完成时被调用
    # bot : QQBot 对象，提供 List/SendTo/GroupXXX/Stop/Restart 等接口，详见文档第五节
    DEBUG('START-UP-COMPLETE')

def onUpdate(bot, tinfo):
    # 某个联系人列表更新时被调用
    # bot : QQBot 对象，提供 List/SendTo/GroupXXX/Stop/Restart 等接口，详见文档第五节
    # tinfo : 联系人列表的代号，详见文档中关于 bot.List 的第一个参数的含义解释
    DEBUG('ON-UPDATE: %s', tinfo)

def onPlug(bot):
    # 本插件被加载时被调用，提供 List/SendTo/GroupXXX/Stop/Restart 等接口，详见文档第五节
    # 提醒：如果本插件设置为启动时自动加载，则本函数将延迟到登录完成后被调用
    # bot ： QQBot 对象
    DEBUG('ON-PLUG : qqbot.plugins.sampleslots')

def onUnplug(bot):
    # 本插件被卸载时被调用
    # bot ： QQBot 对象，提供 List/SendTo/GroupXXX/Stop/Restart 等接口，详见文档第五节
    DEBUG('ON-UNPLUG : qqbot.plugins.sampleslots')

def onExpire(bot):
    # 登录过期时被调用
    # 注意 : 此时登录已过期，因此请勿在本函数中调用 bot.List/SendTo/GroupXXX/Stop/Restart 等接口
    #       只可以访问配置信息 bot.conf
    # bot : QQBot 对象
    DEBUG('ON-EXPIRE')
        
def insertChatAdContent(bot,contact,member,content,keyword):
    # 连接数据库  
    connect = pymysql.Connect(  
        host='localhost',  
        port=3306,  
        user='root',  
        passwd='root',  
        db='qq_data',  
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