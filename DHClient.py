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
x = int(input("Introduce X: "))

z1 = expMod(n, x, p)
print("Z1 =", z1)

z2 = int(input("Introduce Z externo:"))

z = expMod(z2, x, p)
print("Z común =", z)
