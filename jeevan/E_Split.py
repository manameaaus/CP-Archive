t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))

    freq = [0] * (n+1)

    for i in l:
        freq[i] += 1

    if n % k:
        print(0)
    else:
        val = []
        for i in freq:
            if i != 0:
                val.append(i)
                if i % k != 0:
                    print(0)
                    break
        else:
            maxa = [i//k for i in freq]
            curr = [0] * (n+1)

            ans = 0

            p = 0
            q = 0
            while q < n:
                if curr[l[q]] + 1 > maxa[l[q]]:
                    while l[p] != l[q]:
                        curr[l[p]] -= 1
                        p += 1
                    curr[l[p]] -= 1
                    p += 1
                else:
                    diff = q-p+1
                    ans += diff
                    curr[l[q]] += 1
                    q += 1

            print(ans)


