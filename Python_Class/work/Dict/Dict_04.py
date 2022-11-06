

dict = {'性别':['女','女','男','男','男','女','女','男','男','男',],'书本':[10,200,200,50,200,100,200,300,100,200],'文具':[30,10,100,20,50,10,100,50,10,50],'服饰':[300,300,1000,300,400,500,500,0,500,200],'零食':[100,300,100,100,100,150,300,10,40,100],'日用品':[600,100,200,200,200,800,200,50,500,100]}
book = dict['书本']
sum1 = 0
for i in range(len(book)):
    sum1 = sum1 + book[i]
print("书本的平均消费")
print(sum1/len(book))

stat = dict['文具']
sum2 = 0
for i in range(len(stat)):
    sum2 = sum2 + stat[i]
print("文具的平均消费")
print(sum2/len(stat))

clothes = dict['服饰']
sum3 = 0
for i in range(len(clothes)):
    sum3 = sum3 + clothes[i]
print("服饰的平均消费")
print(sum3/len(clothes))

snacks = dict['零食']
sum4 = 0
for i in range(len(snacks)):
    sum4 = sum4 + snacks[i]
print("零食的平均消费")
print(sum4/len(snacks))

daily = dict['日用品']
sum5 = 0
for i in range(len(daily)):
    sum5 = sum5 + daily[i]
print("日用品的平均消费")
print(sum5/len(daily))

n = 0
v = 0
sex = dict['性别']
for i in range(len(sex)):
    if(sex[i] == "男"):
            n = n + book[i] + stat[i] + clothes[i] + snacks[i] + daily[i]
    else:
        v = v + book[i] + stat[i] + clothes[i] + snacks[i] + daily[i]
print("男生的总消费平均值是")
print(n/sex.count("男"))
print("女生的总消费平均值是")
print(v/sex.count("女"))