t = int(input())
for i in range(t):
    n , k = map(int,input().split())
    l = list(map(int,input().split()))
    x = max(l)
    y = min(l)
    su = sum(l)
    if x-y > k+1 or (x-y == k+1 and l.count(x) > 1):
        print("Jerry")
    else:
        if su % 2 == 1:
            print("Tom")
        else:
            print("Jerry")



7
# 8
