# import requests
#
# x = requests.get('https://www.runoob.com/')
#
#
# print(x.status_code)
#
# print(x.reason)
#
# print(x.apparent_encoding)

import requests

x = requests.get('https://www.runoob.com/try/ajax/json_demo.json')


print(x.json())