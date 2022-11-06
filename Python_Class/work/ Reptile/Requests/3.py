# -*- coding:utf-8 -*-
import  requests
import  parsel
import  os

images_dir = 'image' # 文件保存
# for循环 下载多页的图片
for page in range(1,2):
    # response = requests. get(base_url,headers)
    # 请求网站 获得数据
    # f'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html'  f 填空
    response = requests.get(f'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html')
    # 数据解析方式 css xpath re
    sel = parsel.Selector(response.text)
    print(sel)

    # css技术
    # print(sel.css('.ui.segment img').getall())
    # print(sel.xpath('//*[@id="bqb"]/div[1]/div[32]/a/img').getall())

    imgs = sel.css('.ui.segment img')
    print(imgs)
    for img in imgs:
        image_url = img.xpath('./@data-original').get()
        image_name = img.xpath('./@title').get()
        # print(image_url,image_name)
        # 下载图片
        response = requests.get(image_url)
        # 图片视频音频文件都是二进制的，用wb进行保存，写入response.content
        suffix = image_url.split('.')[-1]
        try:
            # open第一个参数path文件夹名/文件名
            # 为什么要加一个判断，判断文件夹是否存在
            # 文件夹文件目录数据库已经存在的东西 创建一个文件夹
            if not (images_dir):
                os.mkdir(images_dir)
            with open(images_dir+'/'+image_name + '.'+suffix, mode='wb',) as f:
                f.write(response.content)
        except:
            pass