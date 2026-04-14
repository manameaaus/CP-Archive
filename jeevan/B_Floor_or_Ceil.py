def till_odd(n):
    c = 0
    while n%2==0 and n>0:
        n = n//2
        c+=1
    return (c,n)


import math
t = int(input())
for i in range(t):
    x,n,m = map(int,input().split())
    mina = 0
    maxa = 0
    doll = True


    
    while n > 0 and m > 0 and x > 0 and doll:
        j = till_odd(x)
        count = j[0]
        joker = j[1]
        
        if count > n+m:
            mina = x // (2**(n+m))
            break
        elif joker == 0:
            x = 0
            mina = 0
        else:
            jomer = 1






















    #         break
    #     left_count = 0
    #     if count >= m:
    #         count -= m
    #         m = 0
    #         n -= count
    #         x = joker//2
    #         n -= 1
    #     else:
    #         m -= count
    #         hot = joker//2 + 1
    #         if hot % 2:
    #             x = joker//2 + 1
    #             m -= 1
    #         else:
    #             x = joker//2
    #             n -= 1

    # if n==0:
    #     while m>0 and x>0:
    #         x = math.ceil(x/2)
    #         m -= 1
    #     mina = x
    # elif m == 0:
    #     while n>0 and x>0:
    #         x = math.floor(x/2)
    #         n -= 1
    #     mina = x
    # else:
    #     mina = x

    # print(mina)




            


        
 


