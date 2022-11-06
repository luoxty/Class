listinfo = [133,88,24,33,232,44,11,44]
def func(x):
 for i in range(len(x)):
    if(x[i]<100 & x[i]%2==0 ):
        return 1
    else:
        del x[i]

    return x
print(func(listinfo))
