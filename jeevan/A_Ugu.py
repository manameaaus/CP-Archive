t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    start = s[0]
    t = ""
    for i in range(n):
        if s[i] != start:
            t += start
            start = s[i]
    if s[i] == start:
            t += start

    # print(t)
    if t[0] == "0":
        print(max(len(t)-2,0))
    else:
        print(len(t)-1)
