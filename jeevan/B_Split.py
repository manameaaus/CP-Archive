t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))

    d = [0] * (2*n + 1)
    for i in l:
        d[i] += 1
    
    odd = 0
    four = 0
    eve = 0

    for i in range(2*n + 1):
        if d[i]:
            if d[i] % 2 == 1:
                odd += 1
            elif d[i] % 4 == 0:
                four += 1
            else:
                eve += 1

    if four % 2:
        if odd >= 2:
            print(eve * 2 + odd + four * 2)
        else:
            print(eve * 2 + odd + (four-1) * 2)
    else:
        print(eve * 2 + odd + four * 2)