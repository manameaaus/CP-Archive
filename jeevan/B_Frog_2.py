n,k = map(int,input().split())
h = list(map(int,input().split()))

b = [sum(h)*2] * (n)
b[-1] = 0
b[n-2] = abs(h[-1] - h[-2])


for i in range(n-3,-1,-1):
    for j in range(1,k+1):
        if i + j < n:
            b[i] = min(b[i],abs(h[i]-h[i+j]) + b[i+j])

print(b[0])
