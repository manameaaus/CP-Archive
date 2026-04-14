t = int(input())
for i in range(t):
    n = int(input())
    d = {}
    l = map(int,input().split())
    
    for i in d:
        if d[i]>1:
            print("YES")
            break
    else:
        print("NO")