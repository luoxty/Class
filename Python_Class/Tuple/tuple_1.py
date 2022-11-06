import random
l = ["老师1","老师2","老师3","老师4","老师5","老师6","老师7","老师18"]
r = [[],[],[]]
for i in l:
    s=random.randint(0,2)
    r[s].append(i)
print(r[0])
print(r[1])
print(r[2])