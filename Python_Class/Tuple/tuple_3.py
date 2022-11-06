s1 = (7,2,3,4,5,78)
s2 = (2,3,5)
s3 = s1 + s2
list(s3)
s4 = []
print(s3)
for i in s3:
  if s3.count(i)==1:
    s4.append(i)
print(tuple(s4))
