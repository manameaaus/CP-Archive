t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))

    bit_off = [0] * 31
    for bit in range(31):
        for num in l:
            if not ((num >> bit) & 1):
                bit_off[bit] += 1


    ans = 0
    
    for bit in range(30,-1,-1):
        if k >= bit_off[bit]:
            k -= bit_off[bit]
            bit_off[bit] = 0

        if not bit_off[bit]:
            ans |= 1 << bit


    print(ans)

