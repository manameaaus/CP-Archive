MAXN = 100001

spf = [i for i in range(MAXN)]
for i in range(2,MAXN):
    if spf[i] == i:
        for j in range(i*i,MAXN,i):
            spf[j] = min(i,spf[j])

def factorise(num):
    d = {}
    while num > 1:
        d[spf[num]] = d.get(spf[num],0) + 1
        num //= spf[num]
    return d



n,m = map(int,input().split())
activated = [0] * (n+1)
primes = [0] * (n+1)
for _ in range(m):
    opt,num = input().split()
    num = int(num)

    if opt == "+":
        if activated[num]:
            print("Already on")
        else:
            factors = factorise(num)

            for prime in factors:
                if primes[prime]:
                    print(f"Conflict with {primes[prime]}")
                    break
            else:
                print("Success")
                for prime in factors:
                    primes[prime] = num
                activated[num] = 1
    else:
        if activated[num] == 0:
            print("Already off")
        else:
            factors = factorise(num)
            for prime in factors:
                if primes[prime] == num:
                    primes[prime] = 0
            activated[num] = 0
            print("Success")





