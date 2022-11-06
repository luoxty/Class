
# -*- coding:utf-8 -*-

# UA: User-Agent (请求身份标识)
# UA 检测 : 门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份表示为某一款
#    浏览器，说明该请求是一个正常的请求，但是如果检测到请求的载体不是基于某一款浏览器，则表示该
#    请求为不正常（爬虫），则服务器就很有可能拒绝该请求

# UA伪装 : 让爬虫对应的求情载体的身份标识伪装成某一款浏览器

import  requests
if __name__ == "__main__":
 url = 'https://www.sogou.com/web?query=波晓张'

 # UA 伪装 : 将对应的请求 User-Agent 封装到一个字典中
 hander = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.172.400 QQBrowser/11.1.5140.400'
 }

 # 处理 url 携带的参数 : 封装到字典中
 kw = input('enter a word:')
 param = {'query':kw}

 # 都指定的 url 发起的请求是携带参数的，并且在请求过程中处理了参数
 response =  requests.get(url=url,params=param,hander=hander)

 page_text = response.text
 print(page_text)
 filename = kw + '.html'
 with open('Wenbeng/filename.txt', 'w', encoding='utf-8') as fp:
     fp.write(page_text)
 print(filename,)