d = {'login.py': 'a 8 d 2 u 3', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5'}
def func(x):
 sum = 0
 list1 = []
 list2 = []
 for key,value in x.items():
  list1.append(key)
  list2.append(value)
 for i in range(len(list1)):
   for i in range (len(list2)):
      if list2[i].isdigit():
          sum +=  int(list2[i])
 print(list1[i] + str(sum))
func(d)
