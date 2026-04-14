t =  int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    l = [False] * n

    c = 0
    lord = ""
    ans = []
    for i in range(n):
        if l[b[i]-1]:
            ans.append(c)
        else:
            lord = a[b[i]-1]
            while lord != b[i]:
                l[lord-1] = True
                lord = a[lord-1]
                c += 1

            l[lord-1] = True
            c += 1
            ans.append(c)
        
    print(*ans)


