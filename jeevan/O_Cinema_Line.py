n = int(input())
a = list(map(int,input().split()))
c25 = 0
c50 = 0
for i in range(n):
    if a[i] == 25:
        c25 += 1
    elif a[i] == 50:
        if c25 == 0:
            print("NO")
            break
        else:
            c25 -= 1
        c50 += 1
    elif a[i] == 100:
        if (c50 >= 1 and c25 >= 1):
            c50 -= 1
            c25 -= 1
        elif c25 >= 3:
            c25 -= 3
        else:
            print("NO")
            break
else:
    print("YES")