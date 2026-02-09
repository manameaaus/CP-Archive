t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1,n+1):
        print(i,end=" ")
    print()
    # ko = set(a)
    # hoty = 0
    # l = [i for i in range(1,n+1) if i not in ko]
    # for i in a:
    #     if i in ko:
    #         print(i,end=" ")
    #         ko.remove(i)
    #     else:
    #         print(l[hoty],end=" ")
    #         hoty +=  1
    # print()