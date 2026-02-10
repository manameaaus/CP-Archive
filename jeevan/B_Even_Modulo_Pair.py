t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    even = sum(1 for i in a if i % 2 == 0)
    if even > 1:
        dabba = []
        for i in a:
            if i % 2 == 0:
                dabba.append(i)

        print(dabba[0],dabba[1])
    else:
        got = 0

        for i in range(min(1000, n)):
            for j in range(i+1, min(1000, n)):
                if ((a[j] % a[i]) % 2 == 0):
                    print(a[i],a[j])
                    got = 1
                    break

            if got == 1:
                break

        else:
            print(-1)

