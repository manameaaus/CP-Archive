import math
n = int(input())
s = input()

x = s.count('+')
y = s.count('-')

tot = x-y

q = int(input())
for i in range(q):
    a,b = map(int,input().split())

    if tot != 0 and a == b:
        print("NO")
    else:
        if (tot == 0) or ((tot * b) % (b-a) == 0 and (tot * b) // (b-a) >= -y and (tot * b) // (b-a) <= x):
            print("YES")
        else:
            print("NO")







# (k1 - k2) x + (p - k1 - m + k2) y = 0
# -(k2 - k1) x + (p - m) y + (k2 - k1) y = 0
# (k2 - k1) (y - x) + tot y = 0
# tot y = (k1 - k2) (y - x)
# tot * y / (y-x) = (k1 - k2)
