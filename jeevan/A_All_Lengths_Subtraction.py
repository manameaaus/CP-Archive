t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    st = 0

    for i in range(n):
        l = 0
        r = 0
        for j in range(0,i):
            if arr[j] > arr[i]:
                l += 1

        for j in range(i+1,n):
            if arr[j] > arr[i]:
                r += 1

        if l!= 0 and r!=0:
            print("NO")
            break
    else:



        print("YES")
        
