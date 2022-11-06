# 5.写一个函数完成三次登陆功能,再写一个函数完成注册功能
name = "123"
power = "456"
def login(name,power):
 count = 0
 while 1:
  count += 1
  if count <= 3:
   n = input('请输入用户名:')
   p = input('请输入密码:')
   if n == name  and p == power:
     print("登录成功")
   else:
    print("登录失败")
  else:
   return '三次验证失败,请明天再来吧!!!'
login(name,power)
