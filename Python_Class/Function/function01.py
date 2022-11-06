
#定义函数
# def area_of_square(x):
#     s = x * 3
#     return s
#
# # 调用函数
# sqr  = area_of_square(20)
# print(sqr)


# def area_of_square():
#     global s
#     w = x*x                #读取全局的x
#     s=w                    #试图修改全局的s=4
#     print(id(s))           #输出变量的地址
#     return w
# x=2
# s=2
# r=area_of_square()
# print(id(s),r)  # 2 ，4

# 元组作为函数参数
def displayinfo(x):
    print(x[0])
    print(x[1])
    print(x)
age = 19
name = 'W'
height =70
displayinfo((age,name,height))

# 列表作为函数参数
# def displayinfo(x):
#     print(x[0])
#     print(x[1])
#     print(x)
# age = 19
# name = 'W'
# height =70
# displayinfo([age,name,height])

# def displayinfo(*x):
#     print(x[0])
#     print(x[1])
#     print(x)
# age = 19
# name = 'W'
# height =70
# displayinfo(age,name,height)

import random
x=[]
for i in range (10):
  x.append(random.randrange(1, 101, 1))
def pyt(x):
 list(x)
 x.sort(reverse=False)
 print(x)
pyt((x))

def getinfo():
    return 1