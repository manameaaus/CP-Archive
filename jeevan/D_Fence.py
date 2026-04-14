n,k = map(int,input().split())
a = list(map(int,input().split()))
curr = sum(a[:k])
mina = curr
j = 1
for i in range(k,n):
    curr = curr - a[i-k] + a[i]
    if curr < mina:
        mina = curr
        j = i-k+2
print(j)


