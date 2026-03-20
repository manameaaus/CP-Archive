# n = int(input())
# if n%4!=0 and (n+1)%4!=0:
#     print("NO")
# else:
#     if n%4==0:
#         print("YES")
#         print((n)//2)
#         l = [i for i in range(1,n+1)]
#         print(*l[:n//4],end=" ")
#         print(*l[n-n//4:])
#         print((n)//2)
#         print(*l[n//4:n-n//4])
#     else:
#         print("YES")
#         print((n)//2)

#         l = []
#         for i in range(1,n//4+1):
#             l.append(i)
#         for i in range(n//4,-1,-1):
#             l.append(n-i)
        
#         print(*sorted(l))
#         print(n-len(l))
#         for i in range(1,n+1):
#             if i not in l:
#                 print(i,end=" ")


# n = int(input())
# if n%4!=0 and (n+1)%4!=0:
#     print("NO")
# else:
#     print("YES")
#     print((n)//2)
#     for i in range(1,n//4+1):
#         print(i,n+1-i,end=" ")
#     if n%4==0:
#         print()
#         print((n)//2)
#         for i in range(n//4+1,n//2+1):
#             print(i,n+1-i,end=" ")
#     else:
#         print(n-n//4)
#         print(n//2+1)
#         for i in range(n//4+1,n//2+1):
#             print(i,n-i,end=' ')


n = int(input())
if n%4!=0 and (n+1)%4!=0:
    print("NO")
else:
    print("YES")
    k = n*(n+1)//4
    lis  = []
    lis2 = []
    s=0

    for i in range(n,0,-1):
        if s+i<=k:
            s+=i
            lis.append(i)
        else:
            lis2.append(i)
    
    print(len(lis))
    print(*lis)
    print(len(lis2))
    print(*lis2)


    


    






