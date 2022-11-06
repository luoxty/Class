# 5.找出以字母e结尾的单词，忽略大小写


import re
line = 'Age egg alsE TIME holle thank ecpect'
res = re.compile(r'\w+e\b', re.I)
ret = res.findall(line)
print(ret)
while 1:
    l = input("输入字符串")
    if(l == "q"):
        break
    else:
        res = re.compile(r'\w+e\b', re.I)
        ret = res.findall(l)
        print(ret)