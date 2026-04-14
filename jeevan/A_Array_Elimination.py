import math
t = int(input())
for i in range(t):
    n = int(input())
    l = sorted(map(int,input().split()))
    bits = [0] * 31

    for bit in range(31):
        for num in l:
            if ((num >> bit) & 1):
                bits[bit] += 1
    ans = 0
    for count in bits:
        ans = math.gcd(ans,count)

    if not ans:
        print(*range(1,n+1))
    else:
        k = []
        for i in range(1,int(math.sqrt(ans) + 1)):
            if ans % i == 0:
                k.append(i)
                if i != ans//i:
                    k.append(ans//i)

        print(*sorted(k))


