a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]

# 返回一个对象
zipped = zip(a,b)
zipped
# <zip object at 0x103abc288>

# list() 转换为列表
list(zipped)
[(1, 4), (2, 5), (3, 6)]

# 元素个数与最短的列表一致
list(zip(a,c))
[(1, 4), (2, 5), (3, 6)]

# 与 zip 相反，zip(*) 可理解为解压，返回 二维矩阵式
a1, a2 = zip(*zip(a,b))
list(a1)
[1, 2, 3]
list(a2)
[4, 5, 6]

list2 = ['c', 'c', 'b']
print("".join(list2))  # ccb

#元组转字符串
tuple1 = ('a', 'a', 'b')
print(str(tuple1))
