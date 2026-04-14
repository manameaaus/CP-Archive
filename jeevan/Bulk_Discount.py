t = int(input())
for  i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = sorted(a)
    for i in range(n):
        x = c[i]-i
        c[i] = max(0,x) 
    print(sum(c)) 