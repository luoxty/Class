def age(n):
 if n == 1:
  return 10
 else:
  return age(n - 1) + 2


def peach(p):
 if p == 1:
  return 1
 else:
  return (peach(p - 1) + 1) * 2

def ball(b):
    if b == 1:
        return 100
    else:
     ten = ball(b - 1) / 2
 return ten