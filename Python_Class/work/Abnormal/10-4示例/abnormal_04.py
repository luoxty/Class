def len1(zd):
    try:
     for k in zd:
        if len(zd[k])>2 :
            zd[k] = zd[k][:2]
        else:
            raise Exception("字典值长度小于二的！")
     return zd
    except Exception as err:
     print(err)

zd = {"k1":"v1v1","k2":[11,22,33,44]}

print(len1(zd))