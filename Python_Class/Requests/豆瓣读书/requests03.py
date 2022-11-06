import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
import requests
from lxml import etree

# 1.获取豆瓣读书网页内容
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
    "Referer": "https://www.douban.com/"
}
url = "https://book.douban.com/"
response = requests.get(url, headers=headers)
text = response.text
# with open("book.html", "w") as fp:
#     fp.write(response.content)

# 2.通过一定规则获取html文件中的内容
html = etree.HTML(text)

ul = html.xpath("//ul[@class='list-col list-col5 list-express slide-item']")[0]
 #print etree.tostring(ul, encoding="utf-8").decode("utf-8")
# 保存成html文件
# with open("ul.html", "w") as fp:
#     fp.write(etree.tostring(ul, encoding="utf-8"))

lis = ul.xpath(".//li")
 #print etree.tostring(lis[0], encoding="utf-8").decode("utf-8")

# 通过循环获取lis下面的元素及属性
books = []
for li in lis:
    meta = li.xpath(".//div[@class='more-meta']")[0]
    # strip()去掉前后的空格
    # /text()爬取中间text文本
    title = meta.xpath(".//h4[@class='title']/text()")[0].strip()
    author = meta.xpath(".//span[@class='author']/text()")[0].strip()
    year = meta.xpath(".//span[@class='year']/text()")[0].strip()
    publisher = meta.xpath(".//span[@class='publisher']/text()")[0].strip()
    abstract = meta.xpath(".//p[@class='abstract']/text()")[0].strip()
    book = {
        "title": title,
        "author": author,
        "year": year,
        "publisher": publisher,
        "abstract": abstract
    }
    books.append(book)

# 3.保存抓取到的books信息
print(books)