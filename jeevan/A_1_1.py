t = int(input())
for i in range(t):
    n = int(input())
    s = list(int(i) for i in input())
    new = [0] * n
    new[0] = s[0]
    new[-1] = s[-1]
    curr = s[0]
    for i in range(1,n-1):
        curr += s[i] | (s[i-1] & s[i+1])
        new[i] = s[i] | (s[i-1] & s[i+1])


    if n != 1:
        curr += s[-1]


    p = new[0]
    for i in range(1,n-1):
        if (not (new[i-1] and new[i+1])) and new[i]:
            p+=1
        else:
            new[i] = 0

    if n != 1:
        p += new[-1]


    print(p,curr)
    # print(new)


