# -需求:爬取搜狗首页的页面数据
#  -*- coding:utf-8 -*-
import requests

if __name__ == "__main__":



 # 1.指定 url
 url = 'https://www.sogou.com/'

 # 2.发起请求
 #  get() 方法返回一个响应对象
 response =  requests.get(url=url)

 # 3.获取响应数据,text返回字符串形式的响应数据
 page_text = response.text
 print(page_text)

 # 4.持久化存储
 with open('Wenbeng/sougou.html', 'w+', encoding='utf-8') as fp:
     fp.write(page_text)


