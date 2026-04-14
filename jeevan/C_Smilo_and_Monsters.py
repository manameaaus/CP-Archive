# t = int(input())

# for _ in range(t):
#     n = int(input())
#     l = list(map(int,input().split()))
#     l.sort()
#     pre = l[::]
#     for i in range(1,n):
#         pre[i] += pre[i-1]

#     ans = sum(l)
#     curr = 0
#     s = sum(l)

#     for i in range(n-1,-1,-1):
#         curr += l[i]
#         if curr >= pre[i-1] - s%2:
#             # ans = min(ans,n - i + ((s+1)//2))
#             if i == 0:
#                 ans = min(ans,n - i + ((curr + 0 + 1)//2))
#             else:
#                 # ans = min(ans,n - i + ((curr + pre[i-1] + 1)//2))
#                 ans = min(ans,n - i + pre[i-1] + ((curr - pre[i-1] + 1)//2))
#             break
        
    
#     print(ans)



t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    pre = l[::]
    for i in range(1,n):
        pre[i] += pre[i-1]
    pre.append(0)

    ans = sum(l)
    curr = 0

    for i in range(n-1,-1,-1):
        curr += l[i]
        if pre[i-1] >= curr:
            ans = min(ans,pre[i-1] + n - i)
        else:
            ans = min(ans,n - i + pre[i-1] + ((curr - pre[i-1] + 1)//2))
    
    print(ans)