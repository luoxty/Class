products=[["iphone",6888],["MacPro",14800],["小米6",2499],["Coffe",31],["Book",60],["Nike",699]]
sum = [];
for i in products:
    print("选择您想购买的商品")
    s = str(input())
    if (s != "q"):
     n= int(s)
     sum.append(products[n])
    else:
        break
print("------ 商品列表--------")
for i in range(len(sum)):
    print(str(sum.index(sum[i])) +"     " + sum[i][0] +"     " + str(sum[i][1]))











































