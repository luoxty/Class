# 2.字符串

var1 = "hello python";
var2 = "hello world"
print("465546\n54547")

a = "Hello"
print("m" in a)
print("m" not in a)

if("m" in a):
    print("m在变量a中");
else:
    print("m不在变量a中")

if("b" not in a):
    print("b不在变量a中");
else:
    print("b在变量a中")

# 无序
"{} {}".format("hello","world")

# "hello","world"，"hello",
"{0} {1} {0}".format("hello","world")

# 字符串.capitalize 字符首字母大写，其他小写
# 字符串.center(字符个数,"填充字符")   字符串居中，其他用空格或者填充字符填充
# 字符串.couunt(子串,开始位,结束位) 统计字串出现的次数
# 字符串.fing(字符串2,开始位)    找子串位置输出索引值，没有返回-1
# islower 全是大写返回true，不是返回flase
# rstrip 去掉右边的字符 lstrip 去掉左边的字符
# replace（"" , "" ,替换次数） 前字符替换为后字符
# split(分割条件，分割次数) 按条件分割字符
a = "123 456 789";
a1 = a.strip(" " ,2);
print(a1)