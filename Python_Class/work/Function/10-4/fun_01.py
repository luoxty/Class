# 1.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def one (x):
    r=[]
    for i in range(len(x)):
        if(i%2==0):
            r.append(x[i-1])
    print(r)
d=[0,1,2,3,4,5,6,7,8,9]
one(d)
