t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    if k%2==1:
        a = [n for i in range(n)]
        a[n-1] = n-1
    else:
        a = [n-1 for i in range(n)]
        a[n-2] = n
    print(*a)



# [1,2,3,4,5,6,7]
# [6 6 6 6 6 7 6]