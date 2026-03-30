t = int(input())


e = 0
o = 0
eo = 0
oe = 0
for i in range(t):
    a,b = map(int,input().split())
    if a % 2 == 0 and b % 2 == 0:
        e += 1
    elif a % 2 and b % 2 == 0:
        oe += 1
    elif a % 2 and b % 2:
        o += 1
    else:
        eo += 1


if ((o+oe) % 2 == 1 and (o+eo) % 2 == 1) and (oe or eo):
    print(1)
elif (o+oe) % 2 == 0 and (o+eo) % 2 == 0:
    print(0)
else:
    print(-1)