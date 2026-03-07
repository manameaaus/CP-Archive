n,k = map(int,input().split())
a = list(map(int,input().split()))

i    = 0
j    = 0
curr = 0
len  = 0

while j<n:
    if curr + a[j] <= k:
        curr += a[j]
        j += 1
    else:
        len  = max(len,j-i)
        curr = max(0,curr - a[i])
        i += 1
    j = max(j,i)
len  = max(len,j-i)


print(len)
        
