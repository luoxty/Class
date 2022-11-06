# 6.将多个重复字母替换成一个字母（比如ddd替换成d）
import re
line = "aaabcdddefggghijjj"
ret = re.sub(r'([a-zA-Z])\1+ ',r'\1',line)
print(ret)
while 1:
    l = input("输入字符串")
    if(l == "q"):
        break
    else:
        line = "aaabcdddefggghijjj"
        ret1 = re.sub(r'([a-zA-Z])\1+ ', r'\1', l)
        print(ret1)