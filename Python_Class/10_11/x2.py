# 将匹配的数字乘以 2
import  re
def double(matched):
        value = int(matched.group('value'))
        return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d)', double, s))#?P获得名称，可以不要
