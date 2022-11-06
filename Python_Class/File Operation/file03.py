import csv

csv_file = csv.reader(open('1.csv','r'))
print(csv_file)
content=[]

for line in csv_file:
    print(line)
    content.append(line)
print("该种文件保存的的数据类型为:\n",content)

csv_file=csv.writer(open("1.csv",'a',newline=''),dialect='excel')

item1 = ['ju',22,"胡锦鹏不穿"]
item2 = ['hu',22,"胡锦鹏不洗"]