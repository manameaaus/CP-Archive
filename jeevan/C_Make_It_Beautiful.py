t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))

    ultima = 1152921504606846975
    new = [0] * 61
    ans = 0

    for i in range(n):
        x = l[i] ^ ultima
        c = 0

        while x:
            if x%2:
                new[c] += 1
            else:
                ans += 1
            c += 1
            x //= 2

    pot = 1
    for i in range(len(new)):
        if k >= new[i] * pot:
            k -= new[i] * pot
            
            ans += new[i]
        else:
            ans += k // pot
            break
        pot *= 2
    print(ans)


    
