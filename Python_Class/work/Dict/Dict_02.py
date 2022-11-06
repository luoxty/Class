person = {"性别":['女','男'],'江苏':[3,8],'浙江':[2,5],'吉林':[1,0],'山东':[0,5],'安徽':[0,4],'福建':[0,2]}
sex = person['性别']
js= person['江苏']
print("江苏的人数:")
print(js[0] + js[1])

zj= person['浙江']
print("浙江的人数:")
print(zj[0] + zj[1])
jl= person['吉林']
print("吉林的人数:")
print(jl[0] + jl[1])
sd= person['山东']
print("山东的人数:")
print(sd[0] + sd[1])
ah= person['安徽']
print("安徽的人数:")
print(ah[0] + ah[1])
fj= person['福建']
print("福建的人数:")
print(fj[0] + fj[1])
print("男生人数：")
n = js[1] + zj[1] + jl[1] + sd[1] + ah[1] + fj[1]
print(n)
print("女生人数：")
v = js[0] + zj[0] + jl[0] + sd[0] + ah[0] + fj[0]
print(v)
print("总人数：")
print(n + v)