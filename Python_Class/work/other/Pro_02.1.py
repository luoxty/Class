a = "123 456 789 软件204 DongJianm";

a1 = a.lower();
print("a1=  " + a1);

a2 = a.upper();
print("a2=  " + a2);

a3 = a.split( " ",2);
print( a3);

a4 = a.rstrip("m");
print("a4=  " + a4)

a5 = a.replace("软件","计算机");
print("a5=  " + a5)

a6 = a.lstrip("1");
print("a6=  " + a6)

a7 = "{0} {1} {2} {0}".format("123456789","软件204","dongjianm")
print("a7=  " + a7)

a8 = a.find("d");
print( a8)

a9 = a.count("4" ,1)
print( a9)

a10 = a.center(50,"$");
print("a10=  " + a10)