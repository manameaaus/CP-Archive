MOD = 1000000007
t = int(input())
for i in range(t):
    n,m,k = map(int,input().split())
    st = 0
    for i in range(m):
        p,q,r = map(int,input().split())
        st += r

    p = m / ((n * (n-1)) // 2)
    q = ((n * (n-1)) // 2) - m

    res = st
    for i in range(1,k):
        res += res + p
    
