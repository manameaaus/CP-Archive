t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    ans = [0] * (n-1)
    ans[0] = 1

    for i in range(1,n-1):
        if s[i] == s[i-1]:
            ans[i] = ans[i-1]
        else:
            ans[i] = i+1

    print(*ans)