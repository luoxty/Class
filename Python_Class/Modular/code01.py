def sum(x):
    list(x);
    s = 0
    for i in range(len(x)):
        l = x[i]
        s = s + l
    print(s)
    return s
def average(x):
    list(x);
    s = 0
    for i in range(len(x)):
        l = x[i]
        s = s + l
    s = s/5
    print(s)
    return s
def m(x):
    list(x)
    print(max(x))
    return  max(x)
import random
def d(x):
    list(x)
    del x[random.randint(0,4)]
    print(x)
    return x