def nck(n,k):
    deno = 1
    for i in range(k):
        deno *= n - i 
        deno //= (i+1)
    return deno

def de(n,k):
    if n == 0:
        return 1
    if n == 1:
        return 0
    
    d0, d1 = 1, 0
    for i in range(2, k + 1):
        d0, d1 = d1, (i - 1) * (d1 + d0)
    return d1
        
n,k = map(int,input().split())
print(sum(nck(n,k) * de(n,k) for k in range(0,k+1)) + 1)