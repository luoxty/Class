y = set()
s =  int(input())
if(s>2):
 for i in range(s):
    for j in range(s):
       if(j>1 & j<i):
         if (i%j == 0):
            break
         y.add(i)

print(y)
