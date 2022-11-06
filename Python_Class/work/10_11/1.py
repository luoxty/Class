# 1.匹配1-50之间的数

import re
line = '0'
ret = re.match(r'(50|[1-4]\d|[1-9])$',line)
print(ret.group())