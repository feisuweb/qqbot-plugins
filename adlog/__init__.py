# -*- coding: utf-8 -*-
import pymysql  
import datetime
def onQQMessage(bot, contact, member, content):
    if contact.ctype == 'group':
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