import math
t = int(input())
for i in range(t):
    n,x =  map(int,input().split())
    a=list(map(int,input().split()))

    j = [i for i in a if i%x==0]
    if len(j)<2:
        print(-1)
    else:
        for i in range(1,len(j)):
            if math.gcd(j[0],j[i])  == x:
                print(len(j))
                break
        else:
            print(-1)