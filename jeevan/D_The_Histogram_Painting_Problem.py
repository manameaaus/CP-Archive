# n = int(input())
# l = list(map(int,input().split()))
# dp = [1] * n
# ans = n
# for i in range(n):
#     if dp[i]:
#         x = 1
#         for j in range(i+1,n):
#             if l[i] == l[j]:
#                 x += 1
#             if l[j] < l[i]:
#                 print(i,l[i],j,1)
#                 break
#         if x >= l[i]:
#             ans -= x
#             ans += l[i]
#             for j in range(i+1,n):
#                 if l[i] == l[j]:
#                     dp[j] = 0
#                 if l[j] < l[i]:
#                     print(i,l[i],j,2,ans,x)
#                     break
# print(ans)
        
      
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def calc(l,r):
    if l > r:
        return 0
    mina = 1000000001
    idx = -1
    for i in range(l,r+1):
        if arr[i] < mina:
            mina = arr[i]
            idx = i

    for i in range(l,r+1):
        arr[i] -= mina
    
    ccc = calc(l,idx-1) + calc(idx+1,r) + mina
    for i in range(l,r+1):
        arr[i] += mina
    return min(ccc,r-l+1)

    


n = int(input())

arr = list(map(int,input().split()))
print(calc(0,n-1))

    