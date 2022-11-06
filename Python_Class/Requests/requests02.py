import requests
from lxml import etree

# 1.将目标网站上的页面抓取下来
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
    "Referer": "https://movie.douban.com/"
}
url = "https://movie.douban.com/cinema/nowplaying/beijing/"
response = requests.get(url, headers=headers)
text = response.text
with open("responses.html", "w") as fp:
    fp.write(str(response.content))
    # 注意response.content数据类型和response.text数据类型

# 2.将抓取下来的数据根据一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title", encoding="utf-8")[0]
    score = li.xpath("@data-score", encoding="utf-8")[0]
    duration = li.xpath("@data-duration", encoding="utf-8")[0]
    region = li.xpath("@data-region", encoding="utf-8")[0]
    thumbnail = li.xpath(".//img/@src")[0]
    movie = {
        "title": title,
        "score": score,
        "duration": duration,
        "region": region,
        "thumbnail": thumbnail
    }
    movies.append(movie)
print(movies)

