n,k = map(int,input().split())
a = list(map(int,input().split()))

i    = 0
j    = 0
curr = 0
len  = 10000000000 

while j<n and i<=j:
    if curr + a[j] < k:
        curr += a[j]
        j += 1
    else:
        len  = min(len,j-i+1)
        curr = max(0,curr - a[i])
        i += 1
    j = max(j,i)

while i<n and curr>=k:
    len = min(len,j-i+1)
    curr = max(0,curr - a[i])
    i += 1

if len == 10000000000:
    print(-1)
else:
    print(len)
        
