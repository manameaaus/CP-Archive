t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    d = {}
    for i in range(n-1):
        if s[i] in d:
            print("Yes")
            break
        else:
            d[s[i]] = 1
    else:
        if (s[-1] in d and s[-1] != s[0]):
            print("Yes")
        else:
            print("No")


