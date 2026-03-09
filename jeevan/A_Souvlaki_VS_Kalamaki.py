t = int(input())
for i in range(t):

    n = int(input())
    l = list(map(int,input().split()))

    l.sort()
    for i in range(1,n,2):
        if i+1 < n and l[i] != l[i+1]:
            print("NO")
            break
    else:
        print("YES")
        
