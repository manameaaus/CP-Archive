# t = int(input())
# for i in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     mina = 1e8
#     ulti = True

    

#     for i in range(n):

#         if ulti == False:
#             break


#         num  = a[i]
#         lis = [a[i]-1,a[i],a[i]+1]
#         tempmin = 1e8

#         for k in range(3):
#             if (i<n-1 and lis[k] == a[i+1]) or (i > 0 and lis[k] == a[i-1]):
#                 mina = 0
#                 ulti = False
#                 break
        
#         flag = False
#         for j in range(i+1,n-1):
#             kk = min(a[j],a[j+1])
#             kb = max(a[j],a[j+1])

#             for k in range(3):
#                 if lis[k] >= kk and lis[k] <= kb:
#                     tempmin = min(tempmin,j-i)
#                     flag = True
#                     break
#             if flag:
#                 break

        
#         flag = False
#         for j in range(i-1,0,-1):
#             kk = min(a[j],a[j-1])
#             kb = max(a[j],a[j-1])
#             for k in range(3):
#                 if lis[k] >= kk and lis[k] <= kb:
#                     tempmin = min(tempmin,i-j)
#                     flag = True
#                     break
#             if flag:
#                 break


#         mina = min(mina,tempmin)

    
#     if mina == 1e8:
#         print(-1)
#     else:
#         print(mina)


print(200)
for i in range(200):
    print(1000)
    for j in range(1,1001):
        print(j*100,end = " ")
    print()