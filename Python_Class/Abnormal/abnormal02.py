import   math
try:
    d=float(input("请输入三角形的第一条边："))
    if d<=0:
        raise Exception("请输入一个大于零的数！")
    f=float(input("请输入三角形的第二条边："))
    if f<=0:
        raise Exception("请输入一个大于零的数！")
    g=float(input("请输入三角形的第三条边："))
    if g<= 0:
        raise Exception("请输入一个大于零的数！")
    if (d+f)>g and(d+g)>f and (f+g)>d:
                q=d+f+g;
                s=math.sqrt(q/2*(q/2-d)*(q/2-f)*(q/2-g));
                print("该三角形的周长为：",q);
                print("面积为：",s)
    else:
        raise Exception("该三角形不成立！")
except Exception as err:
        print(err)
