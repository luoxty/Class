data = {'login.py': 'a 8 d 2 u 3', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5'}
def fun(x):
 for k, v in x.items():
    sum = 0
    for i in x[k]:
        x[k].split(' ')
        if i.isdigit():
            sum += int(i)
    print('文件：%s,共变更%d行' % (k, sum))
fun(data)
print(data.items())