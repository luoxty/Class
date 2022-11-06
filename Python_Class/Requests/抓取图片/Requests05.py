# -*- coding:utf-8 -*-
import requests
import re
# 第一个爬取网址
url = 'http://www.nipic.com/photo/jingguan/ziran/index.html'
# 获得网页源码
data = requests.get(url).text
regex = r'data-src="(.*?.jpg)"'
# re是一个列表
# 将ma中图片网址依次提取出来
pa = re.compile(regex)
ma = re.findall(pa, data)
i = 0
for image in ma:
    i += 1
    image = requests.get(image).content
    print(str(i) + '.jpg 正在保存。。。')
    with open('d:/pic/' + str(i) + '.jpg', 'wb') as f:
     f.write(image)
print('保存完毕')
