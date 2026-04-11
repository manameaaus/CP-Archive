t = int(input())
import math
for i in range(t):
    k,a,b,x,y = map(int,input().split())

    if x < y:
        t = x
        p = y
        st = a
        en = b
    else:
        t = y
        p = x
        st = b
        en = a


    ans = max(math.floor((k-st) / t)+1,0)
    k -= t*ans

    ans += max(math.floor((k-en) / p)+1,0)


    print(ans)




    