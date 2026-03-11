t = int(input())
for i in range(t):
    n , k = map(int,input().split())
    h = list(map(int,input().split()))
    p = list(map(int,input().split()))

    ulti = [[p[i],h[i]] for i in range(n)]

    ulti.sort()

    st = 0

    used = k

    while k > 0 and st < n:
        while st < n:
            if ulti[st][1] > used:
                break
            else:
                st += 1
        if st < n:
            k -= ulti[st][0]
            used += k

    if k > 0:
        print("YES")
    else:
        print("NO")