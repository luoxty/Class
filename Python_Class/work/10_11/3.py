# 将连续5个以上数字替换成$

import re
line = "111111a12b333333c45d666666"
ret = re.sub(r'\d{5,}','$' , line)
print(ret)
while 1:
    l = "input()"
    if(l == "q"):
        break
    else:
        ret = re.sub(r'\d{5,}', '$', line)
        print(ret)

