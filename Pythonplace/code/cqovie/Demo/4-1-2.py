# find(str,stare,end)
var1 = "helloworld"
var2 = "low"
print("检测low:",var1.find(var1))#0
print("检测low：",var1.find(var2,1,4))#-1
print("检测o：",var1.find("o"))#4

#lower()将字符串中的字母全部转化为小写
var1 = "AvCdEf"
print(var1.islower())#False
print(var1.lower())#avcdef

#islower()判断字符串是否为小写
print(var1.lower().islower())#True

#upper()将字符串中的字母全部转化为大写
print(var1.upper())#AVCDEF

#isupper()判断字符串是否为小写
print(var1.isupper())#False
print(var1.upper().isupper())#True

#split(sep,num)根据sep分割字符串
var1 = "www.cqvie.edu.cn"
print(var1.split("."))
print(var1.split(".",2))

#replace（old,new,max）
print(var1.replace("cn","com"))
var2 = "It is is is is is an ex"
print(var2.replace("is","was",2))

#strip([chars])
var1 = "...www.cqvie.edu.cn."
print(var1.strip("."))
var2 = "123www.cavie.edu.cn321"
print(var2.strip("123"))