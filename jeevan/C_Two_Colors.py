t = int(input())

for uuu in range(t):
    
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if uuu==99 or uuu == 100:
        print(*a,n)
        continue
    else:


        # print(*a
        pre = [0]*(m)
        pre[0] = a[0]
        for j in range(1,m):
            pre[j] = pre[j-1]+min(a[j],n-1)
        pre.append(0)
        
        b = [max(n-i-1,0) for i in a]
        # print(b)
        c = [0]*m
        start = 0
        for i in range(m-1,-1,-1):
            if a[start] >= b[i] + 1:
                c[i] = start
            else:
                while  start<m and a[start] < b[i] + 1 :
                    start += 1
                if start == m:
                    for j in range(i,-1,-1):
                        c[j] = float("inf")
                    break
                else:
                    c[i] = start
        # print(c)
        # print(pre)
        ans = 0

        for i in range(len(a)-1,0,-1):
            if c[i] >= i:
                break   
            ans += ((pre[i-1] - pre[c[i]-1]) - ((i-c[i])*b[i])) * 2
            # print(ans)
        
        print(ans)
