t = int(input())
for i in range(t):
    n,l,r = map(int,input().split())

    ans = [0] * n
    pre = [0] * n
    d = {}


    ans[0] = 1
    d[0] = 1
    d[1] = 1
    pre[0] = 1
    curr = 1

    for i in range(1,n):
        if i == r - 1:
            if l == 1:
                to_put = pre[i-1]
                # print()
            else:
                to_put = pre[i-1] ^ pre[l-2]

            ans[i] = to_put
            # print(to_put)
            curr ^= to_put

        else:
            st = 1
            while curr ^ st in d:
                st*=2

            d[curr ^ st] = 1
            ans[i] = st
            curr ^= st

        pre[i] = curr

    print(*ans)



