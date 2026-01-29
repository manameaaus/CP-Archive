t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    ans = n
    for i in range(n):
        s = input()
        if ans==n:
            if m-len(s)>=0:
                m-=len(s)
            else:
                ans = i
    print(ans)
