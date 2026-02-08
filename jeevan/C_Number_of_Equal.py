n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

i = 0
j = 0
ans = 0
curr = b[0]
cc = 0

while i<n and j<m:
    if a[i] < b[j]:
        i += 1
    elif a[i] == b[j]:
        cc += 1
        i += 1
        curr = b[j]
    else:
        if b[j] == curr:
            ans += cc
        else:
            cc = 0
        if j<m-1 and b[j]!=b[j+1]:
            cc = 0
        j += 1


if i==n:
    while j<m:
        if b[j] == curr:
            ans += cc
            j += 1
        elif b[j] > curr:
            break



print(ans)