import math
def msb(num):
    res = -1
    while num:
        res += 1
        num >>= 1
    return res


t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    ans = 0
    ms = msb(n)
    for bit in range(ms):
        if 2 * bit >= k:
            t_k = k
            if bit < k:
                t_k -= bit
                extra = bit - t_k
            else:
                extra = bit
    
            while extra:
                ans += math.comb(bit,extra)
                extra -= 1
            ans += 1
            
            # print(bit,ans)


    if ms >= k:
        ans += 1

    print(ans)
    # print(ms,k)



# 11100
# 11110
# 11101
# 11111

# 1110
# 1011
# 1101
# 1111
