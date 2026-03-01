is_prime = [1] * (1001)
primes = []
for i in range(2,1001):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*i,1001,i):
            is_prime[j] = 0

def check(prime):
    for i in range(1,len(primes)):
        if prime - primes[i] - primes[i-1] - 1 == 0:
            return True
    return False

n,k = map(int,input().split())
for i in range(2,len(primes)):
    if primes[i] <= n:
        k -= check(primes[i])


print("YES" if k <= 0 else "NO")
