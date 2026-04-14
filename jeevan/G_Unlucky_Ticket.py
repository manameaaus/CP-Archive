n = int(input())
s = input()

f = sorted([int(i) for i in s[:n]])
s = sorted([int(i) for i in s[n:]])
c = 0
d = 0
for i in range(n):
    if f[i] > s[i]:
        c += 1
    elif f[i] < s[i]:
        d += 1

if d == n or c == n:
    print("YES")
else:
    print("NO")  # NO




