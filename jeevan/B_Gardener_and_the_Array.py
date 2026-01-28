t = int(input())
for i in range(t):
    n = int(input())
    freq = {}
    dabba = []
    for i in range(n):
        l = list(map(int,input().split()))
        for j in range(1,len(l)):
            freq[l[j]] = freq.get(l[j],0) + 1

        dabba.append(l[1:])

    for lis in dabba:
        for num in lis:
            if freq[num] < 2:
                break
        else:
            print("Yes")
            break
    else:
        print("No")
