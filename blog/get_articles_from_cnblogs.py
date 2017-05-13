#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

name = 'artech'
my_cnbolgs = 'http://www.cnblogs.com/' + name

#文章列表，每个元素都是字典，格式：{'title':aaa, 'url':bbb}
article_list = []


def get_articles(name):
    page = get_total_pages_v2(name)    #获得总页数
    for i in range(1, page+1):
        url = 'http://www.cnblogs.com/{}/default.html?page={}'.format(name,i)
        get_one_page_articles(url)


def get_one_page_articles(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    articles = soup.select('a.postTitle2')

    for article in articles:
        data = {
            'title':article.get_text(),
            'url':article.get('href')
        }
        article_list.append(data)
    return article_list


# get_total_pages方法只是截取一个字符，文章页数不能超过9页
def get_total_pages(name):
    url  = 'http://www.cnblogs.com/{}/default.html?page=2'.format(name)
    web  = requests.get(url)
    soup = BeautifulSoup(web.text,'lxml')
    page = soup.select('div.pager')
    num  = page[1].get_text()[4:5]  #总页数，是个字符
    return int(num)


def get_total_pages_v2(name):
    url  = 'http://www.cnblogs.com/{}/default.html?page=2'.format(name)
    web  = requests.get(url)
    soup = BeautifulSoup(web.text,'lxml')
    page = soup.select('div.pager')
    num  = page[1].get_text()[4:5]

##    print(page[1].get_text())
    SEARCH_PAT = re.compile(r'\d+')
    pat_search = SEARCH_PAT.search(page[1].get_text())
    if pat_search != None:
##        print(pat_search.group())
        num = pat_search.group()
    return int(num)


def get_info(name):
    url  = 'http://www.cnblogs.com/mvc/blog/news.aspx?blogApp=' + name
    web  = requests.get(url)
    soup = BeautifulSoup(web.text,'lxml')
    info = soup.select('div > a')
##    nick = info[0].get_text()
##    age = info[1].get_text()
##    followers = info[2].get_text()
##    follwees = info[3].get_text()
    data = [info[i].get_text() for i in range(0,4)]
##    nick,age,followers,follwees = data
    return data


if __name__ == '__main__':
    nick,age,followers,follwees = get_info(name)  # 获取个人信息
    get_articles(name)                            # 获取文章列表
    print('昵称：' + nick, ' 园龄：' + age,' 粉丝：' + followers,\
          ' 关注：' + follwees, ' 文章：' + str(len(article_list)))
    print()
    for i in article_list:
        print(i['title'], i['url'], sep='\n')
        print()