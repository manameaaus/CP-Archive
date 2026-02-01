t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    res = set()
    for i in range(n):
        res.add((l[i]+i+1)%n)
    print("YES" if len(res) == n else "NO")