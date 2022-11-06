import os
n=int(input())
flag=str(input())
keys = []
for i in range(n):
            s=str(input())
            value = s.split(' ',2)
            keys.append(value)
            print(keys)
if(flag==0):
            new=sorted(keys, key=lambda d: int(d[1]),reverse=True)
            for i in range(n):
                print(' '.join(new[i]))
else:
            new=sorted(keys, key=lambda d: int(d[1]),reverse=False)
            for i in range(n):
                print(' '.join(new[i]))

