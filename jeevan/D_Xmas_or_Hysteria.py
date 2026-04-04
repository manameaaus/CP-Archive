t = int(input())
hunt = False

for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [[a[i],i+1] for i in range(n)]

    b.sort()


    if m*2 > n:
        print(-1)
    else:
        if m:
            print(n-m)
            for i in range(0,m-1):
                print(b[n-1-i][1] , b[i][1])

            for i in range(m,n-m+1):
                print(b[i][1],b[i-1][1])
        else:
            ans = []
            tar = b[-1][0]
            for i in range(n-2,-1,-1):
                if b[i][0] >= tar:
                    for j in range(0,i):
                        ans.append([b[j][1],b[j+1][1]])
                    for j in range(i,n-1):
                        ans.append([b[j][1],b[-1][1]])
                    break
                else:
                    tar -= b[i][0]

            if ans:
                print(len(ans))
                for x,y in ans:
                    print(x,y)
            else:
                print(-1)

        



            


