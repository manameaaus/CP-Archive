n , x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
i = 0
j = n-1
ans = 0
while i <= j :
    ans += 1
    if a[i] + a[j] <= x:
        i += 1
        j -= 1
    else:
        j -= 1

print(ans)





        


