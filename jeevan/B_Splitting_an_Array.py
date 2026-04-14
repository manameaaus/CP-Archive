def check(mid,x):
    curr = 0
    cnt = 1
    for i in arr:
        if curr + i <= mid:
            curr += i
        else:
            cnt += 1
            curr = i
    if cnt <= x:
        return True
    return False


n,k = map(int,input().split())
arr = list(map(int,input().split()))

i = max(arr)
j = sum(arr)

while i <= j:
    mid = (i+j)//2
    if check(mid,k):
        ans = mid
        j = mid - 1
    else:
        i = mid + 1
print(ans)

