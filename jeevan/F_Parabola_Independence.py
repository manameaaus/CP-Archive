t = int(input())
for i in range(t):
    n = int(input())
    dabba = []
    for i in range(n):
        dabba.append(list(map(int,input().split())))

    test = []
    ans = 0
    for i in range(n):
        curr = 0
        for j in range(n):
            a = dabba[i][0] - dabba[j][0]
            b = dabba[i][1] - dabba[j][1]
            c = dabba[i][2] - dabba[j][2]

            if b * b < 4 * a * c or not a:
                curr += 1
                test.append((i+1,j+1))


        print(curr,end = " ")
    print()

    print(test)