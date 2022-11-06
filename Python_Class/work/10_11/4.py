# 4.取出字符串中的所有字母

import re
line = "111111a12b333333c45d666666"
ret = re.findall(r'[a-zA-Z]',line)
print(ret)
while 1:
    l = input("输入字符串")
    if(l == "q"):
        break
    else:
        ret1 = re.findall(r'[a-zA-Z]', l)
        print(ret1)
