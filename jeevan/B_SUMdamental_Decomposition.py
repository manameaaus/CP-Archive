# t = int(input())
# for i in range(t):
#     n,x = map(int,input().split())
#     ccc = bin(x)[2:].count("1")
#     # print(ccc)
#     if ccc > n:
#         print(x)
#     else:
#         if ccc % 2 == 0 and n % 2 == 0:
#             print(x + (n-ccc))
#         elif ccc % 2 == 0 and n % 2 == 1:
#             print(x + (n-ccc+1))
#         elif ccc % 2 == 1 and n % 2 == 0:
#             print(x + (n-ccc+1))
#         else:
#             print(x + (n-ccc))



# print(9101112 + 12345678-13)



t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    bit = bin(x)[2:].count("1")
    if x==0:
        if n==1:
            print(-1)
        elif n%2==1:
            print(3+n)
        else:
            print(n)
    elif x==1:
        if n==2:
            print(5)
        elif n%2==0:
            print(3+n)
        else:
            print(n)
    else:
        if bit <= n:
            if (bit%2==0 and n%2==0) or (bit%2==1 and n%2==1):
                print(x+(n-bit))
            elif (bit%2 ==0 and n%2 ==1) or (bit %2==1 and n%2==0):
                print(x +(n-bit+1))
        else:
            print(x)
            
            
