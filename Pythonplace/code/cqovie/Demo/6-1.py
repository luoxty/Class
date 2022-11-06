#函数
def isPrime(m):
    print("start")
    for i in range(2,m):
        print(i)
        if m%i ==0:
            return 0
        print("OK")
        return 1
print("return:",isPrime(10))
