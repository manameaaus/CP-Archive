# t = int(input())
# for i in range(t):
#     n , k = map(int,input().split())
#     if k!=1:
#         for i in range(2,n+1):
            # print(i,end=" ")
#         print(1)
#     else:
#         print(-1)

# t = int(input())
# for i in range(t):
#     n , k = map(int,input().split())
#     if k!=1 and n!=1:
#         for i in range(n%k+2,n+1):
#             print(i,end=" ")
#         for i in range(1,n%k+2):
#             print(i,end=" ")
#         print()
#     else:
#         print(-1)

# t = int(input())
# for i in range(t):
#     n , k = map(int,input().split())

#     if k!=1 and n!=1:
#         if k<n:
#             # print(k,k+1,end=" ")
#             # if k!=(n%k)+1:
#             #     print(k,end=" ")
            
#             for i in range(k,0,-1):
#                 if n%k+1!=i:
#                     print(i,end=" ")
            
#             if k+1!=(n%k)+1:
#                 print(k+1,end=" ")
#             for i in range(k+2,n+1):
#                 print(i,end=" ")
#             print((n%k)+1)
#         else:
#             for i in range(2,n+1):
#                 print(i,end=" ")
#             print(1)
#     else:
#         print(-1)

# t = int(input())
# for i in range(t):
#     n , k = map(int,input().split())

    # if k!=1 and n!=1:
#         for i in range(2,n+1,2):
#             print(i,i-1,end=" ")
#     else:
#         print(-1)

t = int(input())
for i in range(t):
    n , k = map(int,input().split())
    if k==1 or n==1:
        print(-1)
    elif n%2==1 and k==2:
        print(-1)
    else:
        if k<n:
            for i in range(3,n+1):
                print(i,end=" ")
            print(1,2)
        else:
            for i in range(2,n+1):
                print(i,end=" ")
            print(1)

