import re
pattern="^[023-]+[0-9]{8}$"
tel=input("请输入电话号码：")
result=re.match(pattern,tel)
if result:
    print("%s是有效电话。"%result.group())
else:
    print("%s是无效电话。" % tel)
