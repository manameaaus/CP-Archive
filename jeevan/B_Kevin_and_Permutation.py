t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    c = 1
    l = [0]*n
    for i in range(k-1,n,k):
        l[i] = c
        c += 1
    for i in range(n):
        if l[i]==0:
            l[i] = c
            c+=1
        
    print(*l)