import re
str = input("输入字符串")

l1 = re.findall(r'\d',str)
l2 = re.findall(r'[A-za-z]',str)
with open('num.txt', 'r+') as f:
    for i in range(len(l1)):
        f.write(l1[i])
    print(f.read())
with open('word.txt', 'r+') as f:
    for i in range(len(l2)):
        f.write(l2[i])
    print(f.read())