spf = [i for i in range(1000001)]
for i in range(2,1000001):
    if spf[i] == i:
        for j in range(i*i,1000001,i):
            spf[j] = min(spf[j],i)


def give_prime_freq(arr):
    freq = {}
    for num in arr:
        while num > 1:
            freq[spf[num]] = freq.get(spf[num],0) + 1
            num //= spf[num]

    return freq


t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    freq = give_prime_freq(l)
    for factor in freq:
        if freq[factor] % n:
            print("NO")
            break
    else:
        print("YES")

