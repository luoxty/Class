# 2.对输入的qq号进行匹配（qq匹配规则：长度为5-10位，纯数字组成，且不能以0开头。)

import re

pattern="^[1-9][0-9]{4,9}$"
qq=input("请输入qq号码：")
result=re.match(pattern,qq)
if result:
    print("%s是有效QQ号。"%result.group())
else:
    print("%s是无效QQ号。" % qq)