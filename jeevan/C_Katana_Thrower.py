n,h = map(int,input().split())
a = []
b = []

for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

a.sort()
b.sort(reverse = True)

rem = 0
ref = -1

for i in range(n):
    if b[i] > a[-1]:
        rem += b[i]
        ref = i
    else:
        rem += 0

    if rem >= h:
        print(i+1)
        break
else:
    print(ref+1 + ((h-rem) + (a[-1]-1)) // a[-1])

