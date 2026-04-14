t = int(input())
for i in range(t):
    n , m = map(int,input().split())
    valid = 0
    for i in range(31):
        if (n * (1 << i)) % m == 0:
            valid = 1
            break
    
    n %= m
    cuts = 0
    temp_n = n
    while valid and temp_n:
        cuts += temp_n
        temp_n *= 2
        temp_n %= m

    print(cuts if valid else -1)


