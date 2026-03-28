n , k = map(int,input().split())
a = list(map(int,input().split()))

pre = [0] * 10**5

uni = 0
i = 0
j = 0
ans = 0
while j<n:
    if uni < k:
        if pre[a[j]] == 0:
            pre[a[j]] += 1
            uni += 1
            j += 1
            ans += j-i
        else:
            pre[a[j]] += 1
            j += 1
            ans += j-i
    elif uni >= k:
        while uni >=k and j<n:
            if pre[a[j]] == 0:
                pre[a[i]] -= 1
                if pre[a[i]] == 0:
                    uni -= 1
                i += 1
            else :
                pre[a[j]] += 1
                j += 1
                ans += j-i

# print(pre[8])

print(ans)






