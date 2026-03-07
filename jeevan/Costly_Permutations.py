# t = int(input())
# for i in range(t):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     xx = [i for i in range(1,n+1)]
#     d = []
#     for i in range(n):
#         if arr[i]==i+1:
#             d.append(i+1)
#             xx.remove(i+1)
#     if len(d)==n:
#         print(1+n)
#     else:
#         if len(d)%2:
#             print(sum(d)+xx[0])
#         else:
#             print(sum(d))

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    xx = [i for i in range(1,n+1)]
    d = []
    for i in range(n):
        if  arr[i]==i+1 or (arr[i]==n-i and n%2==0):
            d.append(i+1)
            xx.remove(i+1)
    if len(d)==n:
        print(sum(d))
    else:
        if len(d)%2:
            print(sum(d)+xx[0])
        else:
            print(sum(d))
