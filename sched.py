# -*- coding: utf-8 -*-
from datetime import datetime

from qqbot import QQBotSched as qqbotsched, RunBot

@qqbotsched(hour='11,17', minute='55')
def mytask(bot):
    gl = bot.List('group', '深圳IT外包-总群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：快下班了...撤退倒计时..')
    gl = bot.List('group', '深圳IT外包-老友群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：快下班了...撤退倒计时..')
    gl = bot.List('group', '深圳IT外包-2群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：快下班了...撤退倒计时..')
    gl = bot.List('group', '深圳IT外包-3群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：快下班了...撤退倒计时..')
    gl = bot.List('group', '深圳IT外包-4群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：快下班了...撤退倒计时..')
    gl = bot.List('group', '深圳IT外包-5群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：快下班了...撤退倒计时..')
    gl = bot.List('group', '深圳IT外包-6群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：快下班了...撤退倒计时..')
    gl = bot.List('group', '深圳IT外包交流群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：快下班了...撤退倒计时..')            
    gl = bot.List('group', '深圳项目外包交流群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：快下班了...撤退倒计时..')

            
@qqbotsched(minute='0-55/5')
def getGroupMembertask(bot):

if __name__ == '__main__':
    RunBot()
