def msb(num):
    # not required , but it works (better)
    bit = -1
    while num:
        num >>= 1
        bit += 1
    return bit

t = int(input())
for i in range(t):
    x,m = map(int,input().split())
    ans = 0
    high = 1<<msb(x)
    for y in range(high,min(m+1,high<<1)):
        if (x ^ y) and ((x % (x^y) == 0) or (y % (x^y) == 0)):
            ans += 1

    print(ans)
    
