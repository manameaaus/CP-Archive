def nck(n,k):
    deno = 1
    for i in range(k):
        deno *= n - i 
        deno //= (i+1)
    return deno


def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return i


n = int(input())
print((n - 3) * 3 * 3 * pow(4,n-3) + 2 * 1 * 3 * pow(4,n-2))