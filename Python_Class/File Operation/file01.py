fo = open("d:\\11.txt","r+")
print("文件名:",fo.name)
str = "a"
print(fo.write(str))


#
str1 = "567"
fo.write(str1)
print(fo.seek(2))
print(fo.tell())
print(fo.read())

#
str2 = "\n"
str3 = "djm"
fo.write(str2)
fo.write(str3)
print(fo.read())
