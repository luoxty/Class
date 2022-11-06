score = [];
score.append(68);
score.append(87);
score.append(92);
score.append(100);
score.append(76);
score.append(88);
score.append(54);
score.append(89);
score.append(76);
score.append(61);

print(score[2])

print(score[0:6])

score.insert(2,59)
print(score);

num = 76;
print(score.count(num));


print(score.index(100))

score[2] = 60;
print(score);

del score[0];
print(score)

print(len(score))

score.sort()
print(score[0])
print(score[9])

print("13题")
score.reverse()
print(score)

print(score.pop())

score.append(88)
print(score)
score.remove(88)
print(score)

score1 = [80,61]
score2 = [71,95,82]
score1.extend(score2);
print(score1)



score3 = [80,61]
score4 = score3.copy()
print(score4)

a = ["01","张三",93]
b = ["03","李四",98]
c = ["05","王五",90]
list1 = [a,b,c]
print(list1)

d = ["07","赵六",88]
list1.insert(1,d)
print(list1)

list1.pop()
print(list1)

list2 =  sorted(list1,key=lambda s: s[2],reverse = True)
print(list2)
