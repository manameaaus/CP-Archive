t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    l = [0]*n
    c = 1
    for i in range(len(s)-1,-1,-1):
        if s[i] != ">":
            l[i+1] = c
            c += 1
    for i in range(n):
        if not l[i]:
            l[i] = c
            c += 1
        print(l[i],end= " ")
    print()
