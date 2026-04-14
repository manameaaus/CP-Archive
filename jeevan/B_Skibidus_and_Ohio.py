n = int(input())
for i in range(n):
    s = input()
    c = 0
    ans = len(s)
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            ans = 1
            break
    print(ans)

        