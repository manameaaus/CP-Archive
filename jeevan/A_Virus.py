t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    # l = [True] * (n)
    # for i in a:
    #     l[i-1] = False

    # start =  a[0]

    got = []

    for i in range(1,k):
        got.append((a[i]-a[i-1]-1))

    got.append(n-a[-1]+a[0]-1)

    
    # c = 0
    # curr = 0
    # while c<n:
    #     if l[start]:
    #         curr += 1
    #     else:
    #         got.append(curr)
    #         curr = 0
    #     start += 1

    #     c += 1
    #     start %= n
    # print((got))

    got.sort(reverse=True)

    ans = 0
    gogogo = 0

    for i in got:
        ans += max(0,i - gogogo*2 -1)
        if i - gogogo*2 -1 == 0:
            ans += 1
        # print(ans)
        gogogo += 2
    print(n-ans)  # print the answer - you can print it out of the loop too
    




