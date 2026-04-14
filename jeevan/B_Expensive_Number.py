t= int(input())
for i in range(t):
    s = [int(i) for i in input()]
    c = 0
    p = 0
    for i in s:
        if i > 0:
            c = 0
        else:
            c += 1
            
    for i in s:
        if i != 0:
            p += 1

    ans = c + p - 1
    

    print(ans)

