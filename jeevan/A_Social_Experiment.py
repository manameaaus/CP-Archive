t = int(input())
for _ in range(t):
    n = int(input())
    ans = n % 2
    if ans == 0:
        if n%4 == 2 and n < 6:
            ans += 2
    else:
        if n%4 == 3 and n < 7:
            ans += 2

    print(ans)
        