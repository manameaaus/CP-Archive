t = int(input())
for i in range(t):
    n = int(input())
    print(bin(n)[2:].count("1"))