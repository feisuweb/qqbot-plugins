# -*- coding: utf-8 -*-
from datetime import datetime

from qqbot import QQBotSched as qqbotsched, RunBot

@qqbotsched(hour='11,17', minute='55')
def mytask(bot):
    gl = bot.List('group', '深圳IT外包-总群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：快下班了...撤退倒计时..')

if __name__ == '__main__':
    RunBot()
