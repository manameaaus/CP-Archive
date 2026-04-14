n = int(input())
h = list(map(int,input().split()))

b = [0] * (n)
b[n-2] = abs(h[-1] - h[-2])
for i in range(n-3,-1,-1):
    b[i] = min(abs(h[i] - h[i+1]) + b[i+1], b[i+2] + abs(h[i] - h[i+2]))

print(b[0])
