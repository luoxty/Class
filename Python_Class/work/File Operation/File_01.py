import random

with open('scores.txt', 'w+') as f:
    for i in range(10):
        li = [random.randint(0, 100) for i in range(10)]
        f.write(str(li[0]) + '\n')

with open('statictic.txt', 'w') as f1, open('scores.txt', 'r') as f2:
    li = f2.readlines()
    # print(li)
    li1 = []
    res = 0
    for i in li:
        i = int(i.strip('\n'))

        li1.append(i)
        res += i

    li1.sort()
    print('最高成绩为：%s' % (li1[-1]))
    print('最低成绩为：%s' % (li1[0]))
    print('平均成绩为：%s' % (res / 100))
    count = 0
    for i in li1:
        if i > 90:
            count += 1
        else:
            pass

    print('90分以上的人数为：%d' %(count))
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    for i in li1:
        if i >= 90:
            one += 1
        elif 90 > i >= 80:
            two += 1
        elif 80 > i >= 70:
            three += 1
        elif 70 > i >= 60:
            four += 1
        else:
            five += 1
    f1.write('优秀人数：%d，良好人数：%d，中等人数：%d，及格人数：%d，不及格人数：%d' % (one, two, three, four, five))
