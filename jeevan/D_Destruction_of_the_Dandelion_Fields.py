t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ans = 0

    odd = []
    for i in l:
        if i%2:
            odd.append(i)
        else:
            ans += i

    if odd:
        odd.sort()
        odd = odd[::-1]
        for i in range((len(odd)+1)//2):
            ans += odd[i]
        print(ans)
    else:
        print(0)