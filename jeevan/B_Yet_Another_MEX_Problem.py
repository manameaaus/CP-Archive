t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    s = set(l)
    for i in range(k-1):
        if i not in s:
            print(i)
            break
    else:
        print(k-1)
    
    