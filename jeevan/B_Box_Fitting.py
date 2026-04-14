BITS = 20

t = int(input())
for i in range(t):
    N, W = map(int, input().split())
    freq = [0] * BITS
    l = list(map(int,input().split()))

    for i in range(N):
        w = l[i]
        b = 0
        while (w & 1) == 0:
            w >>= 1
            b += 1
        freq[b] += 1

    need = 0

    while max(freq) > 0:
        need += 1
        current = W

        for b in range(BITS - 1, -1, -1):
            size = 1 << b
            while current >= size and freq[b] > 0:
                current -= size
                freq[b] -= 1

    print(need)
