# 7.获取长度为3个字母的单词
import re
line = 'Age egg alsE TIME holle thank ecpect'
ret = re.findall(r'\b\w{3}\b' , line)
print(ret)
while 1:
    l = input("输入字符串")
    if(l == "q"):
        break
    else:
        ret1 = re.findall(r'\b\w{3}\b', l)
        print(ret1)