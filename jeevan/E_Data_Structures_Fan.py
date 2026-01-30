t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    s = list(input())

    prefix = arr[::]
    for i in range(1,n):
        prefix[i] ^= prefix[i-1]


    zero = 0
    one = 0
    for i in range(n):
        if s[i] == '1':
            one ^= arr[i]
        else:
            zero ^= arr[i]




    q = int(input())
    for i in range(q):
        k = list(map(int,input().split()))
        if k[0] == 1:
            l,r = k[1],k[2]
            l-=1
            r-=1
            if l == 0:
                to_use = prefix[r]
            else:
                to_use = prefix[r] ^ prefix[l-1]

            zero ^= to_use
            one ^= to_use

        else:
            if k[1] == 0:
                print(zero,end = " ")
            else:
                print(one,end = " ")

    print()