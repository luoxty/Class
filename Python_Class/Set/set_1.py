 # 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

# 集合a中包含而集合b中不包含的元素
print(a - b)
# {'r', 'd', 'b'}

 # 集合a或b中包含的所有元素
print(a | b)
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

# 集合a和b中都包含了的元素
print(a & b)
# {'a', 'c'}

 # 不同时包含于a和b的元素
print(a ^ b)
# {'r','d', 'b', 'm', 'z', 'l'}