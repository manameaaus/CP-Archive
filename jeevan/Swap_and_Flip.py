t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    t = input()
    s = [int(i) for i in s]
    t = [int(i) for i in t]
    if s==t:
        print("YES")
    else:
        c = 0
        for i in range(n):
            if s[i]!=t[i]:
                c+=1
        if c%2:
            print("NO")
        else:
            print("YES")