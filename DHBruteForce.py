import datetime

def expMod(n, x, p):
    n=int(n)
    x=int(x)
    p=int(p)
    if x == 0:
        return 1
    else:
        if (x & 1) != 0:
            r = expMod(n, (x - 1), p)
            return ((n * r) % p)
        else:
            r = expMod(n, (x / 2), p)
            return ((r * r) % p)


n = int(input("Introduce N: "))
p = int(input("Introduce P: "))
z1 = int(input("Introduce Z1: "))
z2 = int(input("Introduce Z2: "))
x1=0
x2=0
zR1=-1
zR2=-1

start = datetime.datetime.now()

while z1 != zR1:
    x1 = x1 + 1
    zR1=expMod(n,x1,p)

print("Found X1:", x1)

while z2 != zR2:
    x2 = x2 + 1
    zR2=expMod(n,x2,p)

print("Found X2:", x2)

zT1 = expMod(z2,x1,p)
zT2 = expMod(z1,x2,p)
print("Z =",zT1)

if zT1==zT2:
    print("Z matches")

end = datetime.datetime.now()

time = end-start

print("Total time:", time)