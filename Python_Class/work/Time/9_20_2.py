#
import random

list1 = []
for i in range(97, 123):
    list1.append(chr(i))  # 得到大写字母字符并放入列表
for i in range(65, 90):
    list1.append(chr(i))  # 得到小写字母字符并放入列表
for i in range(48, 58):
    list1.append(chr(i))  # 得到数字字符并放入列表

for i in range(10):
    str1 = ''.join(random.choices(list1, k=8))  # 随机生成8位密码的列表，并将其转换成字符串的形式
    print(f'第{i + 1}个密码是{str1}')
