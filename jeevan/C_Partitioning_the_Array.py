import math
maxa = 200001
spf = [i for i in range(maxa)]

for i in range(2,maxa):
    if spf[i] == i:
        for j in range(i*i,maxa,i):
            spf[j] = min(spf[j],i)

def prime_factorisation(num):
    d = {}
    while num > 1:
        d[spf[num]] = d.get(spf[num],0) + 1
        num //= spf[num]
    return sorted(d.items())


def calc_suffix(dabba):
    n = len(dabba)
    primes = [i[0] for i in dabba]
    temp_suff = [i[1] + 1 for i in dabba]
    suff = [i[1] for i in dabba]
    for i in range(n-2,-1,-1):
        suff[i] *= temp_suff[i+1]
        temp_suff[i] *= temp_suff[i+1]

    return [primes,suff]

def factorisation(num):
    factors = []
    for i in range(1,int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num//i:
                factors .append(num//i)

    return factors


# t = int(input())
# for i in range(t):
#     n = int(input())
#     l = list(map(int,input().split()))
#     # primes,suff = calc_suffix(prime_factorisation(n))
#     factors = factorisation(n)
#     np = len(factors)
#     ans = 0


#     # print(primes,suff)
#     # print(factors)

#     def check(k):
#         ulti = 0
#         for st in range(k):
#             curr = 0
#             for i in range(1,n//k):
#                 diff = abs(l[st + i*k] - l[st + i*k - k])
#                 curr = math.gcd(curr,diff)
#             ulti = math.gcd(ulti,curr)

                
#         return ulti > 1 or ulti == 0
    
#     for k in factors:
#         if check(k):
#             ans += 1
#             # print(k)

#     print(ans)



print(prime_factorisation(10050))
print(prime_factorisation(12000))
print(prime_factorisation(10000))
print(120600000//4)


print(12345//(32 * 125))