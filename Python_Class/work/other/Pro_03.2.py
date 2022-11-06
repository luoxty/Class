sum = [["学号","姓名","成绩"],["01","张三",93],["03","李四",98],["04","王五",90]]
print(sum);
sum.insert(2,["02","小二",100]);
del sum[4];
print(sum);
y = [];
for s in sum[1:]:
    y.append(s[2]);
print(y);
y.sort(reverse=True);
print(y)
