n , k = map(int,input().split())
arr = list(map(int,input().split()))

i , j = 0 , 0
curr , count , ans = 0 , 0 , 0

while j < n:
    if curr + arr[j] <= k:
        curr += arr[j]
        j += 1
        count += 1
        ans += count
    else:
        curr -= arr[i]
        i += 1
        count -= 1
print(ans)

 
# 1 3 6 10 15
