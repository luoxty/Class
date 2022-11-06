# -*- coding:utf-8 -*-


import requests
from bs4 import BeautifulSoup

herder = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'textml,application/xhtml+xml,application/xml;q=0.9,images/webp,images/apng,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1'
}

url = 'https://weibo.com/newlogin?tabtype=list&gid=1028039999&openLoginLayer=0&url=https%3A%2F%2Fwww.weibo.com%2F'
request = requests.get(url, headers=herder)

# print(request.text)

html = request.text
soup = BeautifulSoup(html, 'lxml')
num  = soup.find("div",
               class_="rank num")  # 找到存放排行榜音乐的ul标签,直接返回结果,查询所有包含class的Tag(注意：class在Python中属于关键字，所以加_以示区别 ul = soup.find(attrs={'class': 'col5'})     # 找到存放排行榜音乐的ul标签,
# print(ul)

lis = ul.find_all(name='li')  # 获取每一首音乐对应的标签,find_all() 方法返回结果是包含一个元素的列表

for li in lis:
    paiming = li.find(name='span').string
    name = li.find(name='a', attrs={'href': 'javascript:;'}).string
    a = li.find(name='a', attrs={'class': 'face'})  # 获取存存放连接的a标签,再在a标签里获取连接

    if a != None:
        img = a.find(name='img')  # 获取连接的img标签
        lianjie = img.attrs['src']  # 获取到连接，下面进行一个判断，前十首歌曲有链接，后十首没有
    else:
        lianjie = '没有链接'

    print(paiming, name, lianjie)

    with open('豆瓣音乐信息抓取.txt', 'a', encoding='utf-8') as f:
        f.write(paiming + '\t' + name + '\t' + lianjie + '\n')
        f.close()

