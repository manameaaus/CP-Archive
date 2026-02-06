t = int(input())
for i in range(t):
    s = [int(i) for i in input()]
    n = len(s)
    for i in range(n):
        exp = s[i]
        got = i
        for j in range(i,min(i+9,n)):
            if s[j]-(j-i) > exp:
                exp = max(s[j]-(j-i),exp)
                got = j
        for k in range(got-1,i-1,-1):
            s[k],s[k+1] = s[k+1],s[k]
        s[i] = exp
    print("".join(map(str,s)))