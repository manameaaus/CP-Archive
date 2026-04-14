t =  int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxdiff = 0
    maxl = n
    maxr = n
    for i in range(n):
        big = 0
        small = 0
        for j in range(i+1,n):
            if a[j] > a[i]:
                big += 1
            elif a[j] < a[i]:
                small += 1
            if small - big > maxdiff:
                maxl,maxr = i+1,j+1
                maxdiff = small - big       

    print(maxl,maxr)
    
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     l = list(map(int,input().split()))
#     max_count = 0
#     ind = -1
#     for i in range(len(l)):
#         count = 0
#         for j in range(i+1,len(l)):
#             if l[i]>l[j]:
#                 count+=1
#         if count>max_count:
#             max_count=count
#             ind = i
#     if ind==-1:
#         print(1,1)
#     else:
#         b = ind+1
#         ind2 = 0
#         for i in range(ind+1,len(l)):
#             if l[i]<l[ind]:
#                 ind2=i
#         print(b,ind2+1)