s = input()
t = input()

if len(s) == len(t):
    n = len(s) 
    d = []
    l = []

    for i in range(n):
        if s[i] != t[i]:
            d.append(t[i])
            l.append(s[i])

    if len(d) == 2 and sorted(d) == sorted(l):
        print("YES")
    else:
        print("NO") 
else:
    print("NO")