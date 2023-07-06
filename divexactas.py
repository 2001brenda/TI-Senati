flag1=True
flag2=True
while flag1:
    try:
        a = int(input("valor 1: "))
        flag1=False
    except ValueError:
        print("te equivocaste")

while flag2:
    try:
        b = int(input("valor 2: "))
        flag2=False
    except ValueError:
        print("te equivocaste")

if (a%b)==0:
    print(f"{a} y {b} es una division exacta")
else:
    print(f"{a} y {b} es una division inexacta")
