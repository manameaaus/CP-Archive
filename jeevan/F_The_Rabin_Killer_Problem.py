import math
MAXN = 1000006
sieve = [1] * MAXN
primes = []

for i in range(2,MAXN):
    if sieve[i]:
        primes.append(i)
        for j in range(i*i,MAXN,i):
            sieve[j] = 0 



def isPrime(n):
    d = n-1
    r = 0
    while d%2 == 0:
        r += 1
        d >>= 1
    
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue

        x = pow(a,d,n)
        if x == 1 or x == n-1:
            continue

        for i in range(r):
            x = pow(x,2,n)
            if x == 1:
                break
        else:
            return False
    return True
 
    

def countDivisors(n):
    ans = 1
    for p in primes:
        if n % p == 0:
            k = 0
            while n % p == 0:
                n //= p
                k += 1
            ans *= (k+1)


    if n == 1:
        return ans
    if isPrime(n):
        return ans * 2
    
    root = int(math.isqrt(n))
    if root * root == n and isPrime(root):
        return ans * 3
    
    return ans * 4
n = int(input())
print(countDivisors(n))