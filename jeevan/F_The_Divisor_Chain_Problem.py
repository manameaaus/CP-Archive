t = int(input())
for i in range(t):
    n = int(input())
    steps = [n]
    for bit in range(31):
        if (n >> bit) & 1:
            if n - (1 << bit):
                n -= (1 << bit)
                steps.append(n)
            else:
                for j in range(bit-1,-1,-1):
                    n -= 1 << j
                    steps.append(n)
                break


    print(len(steps))
    print(*steps)

