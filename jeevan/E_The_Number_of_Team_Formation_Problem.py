def nck(n,k):
    deno = 1
    for i in range(k):
        deno *= n - i 
        deno //= (i+1)
    return deno
n = int(input())
print(nck(n,5) + nck(n,6) + nck(n,7))
