def nck(n,k):
    deno = 1
    for i in range(k):
        deno *= n - i 
        deno //= (i+1)
    return deno

n = int(input())
print(nck(5+n-1,5) * nck(3+n-1,3))
