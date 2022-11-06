# 2.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。3.写函数，计算传入函数的字符串中,[数字]、[字母]、[空格]以及[其他]的个数，并返回结果。
def three(x):
 a = 0
 b = 0
 c = 0
 d = 0
 list(x)
 for i in range(len(x)):
  if x[i].isdigit():
   a = a + 1
  else:
   if x[i].isalpha():
    b = b+1
   else:
    if (x[i] == ' '):
     c = c+1
    else:
     d= d+1
 return a,b,c,d

s = "123qazd ,,,"
print(three(s))