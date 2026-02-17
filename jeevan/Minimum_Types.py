# t = int(input())
# for i in range(t):
#     n,x = map(int,input().split())
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
    # d = [[a[i],b[i]] for i in range(n)]
    # d.sort(reverse=True)
    # c = 0
    # j = 0
    # while x>0 :
        
    #     c += 1
    #     x -= d[j][1]*d[j][0]

    #     j+=1
    #     if j==n:
    #         c=-1
    #         break
        
    # print(c)
    

t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    d = [a[i]*b[i] for i in range(n)]
    d.sort(reverse=True)
    c = 0
    j = 0
    while x>0 :
        c += 1
        x -= d[j]
        j+=1
        if j==n:
            if x<=0:
                break
            else:
                c=-1
                break
    print(c)
