import math
n = int(input())
ans = set()
curr = 1
for i in range(n):
    if math.gcd(n,i) == 1:
        curr = (curr * i) % n
        ans.add(i)

if curr != 1:
    ans.remove(curr)
print(len(ans))
print(*sorted(ans))


