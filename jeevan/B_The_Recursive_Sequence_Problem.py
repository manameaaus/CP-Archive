def f(n,r):
    bb = bin(n)[2:]
    res = 0
    for i in range(len(bb)):
        ex = r%2
        r >>= 1
        if bb[i] == "1":
            res += r + ex

    return res
        
    
n, l, r = map(int,input().split())
print(f(n,r) - f(n,l-1))

# print(0 >> 1)

# print(f(25,31))