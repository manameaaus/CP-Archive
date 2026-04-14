n,m = map(int,input().split())
# n,0    m,1

if m<n-1 or m>2*(n+1):
    print(-1)
elif m==n-1:
    print("01"*m+"0")
else:
    while True:
        if m > n > 0:
            print("110",end="")
            m -= 2
            n -= 1
        elif m <= n:
            print("10"*n)            
            break
        else :
            print("1"*m)
            break




    