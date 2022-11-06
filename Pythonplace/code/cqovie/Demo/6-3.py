import myModule
min = myModule.myMin(1,2)
max = myModule.myMax(1,2)
print(min,max)

from  myModule import myMax,myMin
min = myMin(1,2)
max = myMax(1,2)
print(min,max)

# 引入模块中的所有方法
from myModule import *