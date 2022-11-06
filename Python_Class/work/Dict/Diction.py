# 字典一种可变得容器，可以存储任意类型对象；key => value,键唯一不变，重复后覆盖前
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
dict = {'name':'胡锦鹏',}
print(dict)

# 添加记录
dict["sex"] = "男"
print(dict)

# 删除键
del dict['name']
# 清空字典，删除字典的键和值
dict.clear()
# 删除字典
del dict
str(dict)

