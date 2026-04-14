n,m,a,b = map(int,input().split())
x = n%m
ans = b * (n//m)
ans += min(x*a,b)
print(ans)