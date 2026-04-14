t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = "YES"
    for i in range(n):
        if n-1-i>=i:
            if arr[i] <= 2*(n-1-i):
                ans = "NO"
                break
        elif n-1-i<i:
            if arr[i] <= 2*i:
                ans = "NO"
                break
        
    
    print(ans)
