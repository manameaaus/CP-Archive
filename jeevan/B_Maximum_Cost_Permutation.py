t = int(input())
for i in range(t):
    n = int(input())

    arr = list(map(int,input().split()))
    st = n
    en = -1

    z = 0
    f = n
    l = -1

    for i in range(n):
        if arr[i] == 0:
            z += 1
            f = min(f,i)
            l = max(l,i)
        elif i+1 != arr[i]:
            st = min(st,i)
            en = max(en,i)


    if z >= 2:
        print(max(l-f+1,en-st+1,en-f+1,l-st+1))
    else:
        if st == n:
            print(0)
        else:
            if z == 1 and f+1 in arr:
                print(max(en-st+1,en-f+1,f-st+1))
            else:
                print(max(0,en-st+1))


