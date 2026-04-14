t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    if m>(n*(n+1))//2 or m<n:
        print(-1)
    elif n == 1:
        print(1)
    else:
        ans = [0] * n
        for i in range(n-1,-1,-1):
            ans[i] = min(m-i,i+1)
            m -= ans[i]


        # print(ans)
        ans = ans[::-1]
        s = set()
        ggg = []
        for i in range(n,0,-1):
            # if (i != ans[0] and i != ans[1] and i != 1):
            ggg.append(i)
            s.add(i)
        # print(ans)
        print(ans[0])
        if ans[0] == 1:
            s.remove(1)
            ggg.pop()
            ans[1] = ggg.pop()
            # print(ans[1])
            print(1,ans[1])
            s.remove(ans[1])
        else:
            print(ans[0],ans[1])
            s.remove(ans[1])
            s.remove(ans[0])

        

        # if ans[0]!=

        flag = 0
        if ans[0] == 1 or ans[1] ==1:
            flag = 1
        
        for i in range(2,n):
            if ans[i] == 1 and flag:
                x = ggg.pop()
                while x not in s:
                    x = ggg.pop()
                ans[i] = x
                print(ans[i-1],ans[i])

            elif ans[i] == 1:
                print(ans[i-1],1)
                s.remove(ans[i])
                flag = 1
            else:
                # if 
                s.remove(ans[i])
                print(ans[i-1],ans[i])
            






        # xx = m-n+1
        # print(xx)
        # if xx == 1:
        #     print(1,2)
        #     last = 2
        #     for i in range(3,n+1):
        #         print(last,i)
        #         last = i
        # else:
        #     print(m-n+1,1)
        #     last = 1
        #     for i in range(2,n+1):
        #         if i == xx:
        #             continue
        #         else:
        #             print(last,i)
        #             last = i

