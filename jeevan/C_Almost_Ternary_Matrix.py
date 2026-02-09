t = int(input())
for i in range(t):
    n , m = map(int,input().split())
    st = 0
    for i in range(m//4):
        st <<= 4
        st |= 9
    if (m%4):
        st <<= 2
        st |= 2
    
    sd = []
    sa = []

    while (st):
        sd.append((st&1))
        sa.append(1-(st&1))
        st >>= 1

    for i in range(n//4):
        print(*sd)
        print(*sa)
        print(*sa)
        print(*sd)
    if (n%4):
        print(*sd)
        print(*sa)


