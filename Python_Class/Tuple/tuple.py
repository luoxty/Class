# 元组只读,用于存放返回值
tup1 = (1,2,3);
tup2 = ("a","b","c");

#连接元组必须赋给一个新的元组
tup3 = tup1 + tup2;
print(tup3)

#将列表转化为元组
tuple([4,5,6])

print("==========")
lst2 = ['001','2019-11-11',['三文鱼','电烤箱']];
sku = lst2[2];
print(lst2);
print(id(lst2));
print(sku);
print(id(sku))
print(id(sku.append(3)))
print("=================")
lst2 = ['001','2019-11-11',['三文鱼','电烤箱']];
sku1 = lst2[2].copy();
print(lst2);
print(id(lst2));
print(sku1);
print(id(sku1))
print(id(sku1.append(3)))


print("==========")
import random
products=[["iphone",6888],["MacPro",14800],["小米6",2499],["Coffe",31],["Book",60],["Nike",699]]
j = 0;
sum = [];
sum1 = ()
for i in products:
    print("前选择")
    s = str(input())

    if (s != "q"):
     n= int(s)
     sum.append(products[n])
     sum1 = sum
     print(sum1)
    else:
        break
for i in (len(sum1)):
    print (sum1[i])

