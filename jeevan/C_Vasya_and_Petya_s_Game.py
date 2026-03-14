def primes(n):
    is_prime = [1] * (n+1)
    primes = []
    for i in range(2,n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i,n+1,i):
                is_prime[j] = 0
    return primes

n = int(input())
primes = primes(n)
ans = []
for prime in primes:
    curr = prime
    while curr <= n:
        ans.append(curr)
        curr *= prime

print(len(ans))
print(*ans)
