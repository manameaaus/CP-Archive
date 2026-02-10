import math
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))

    def run(num):
        dabba = l[::]
        maxa = 0
        mina = float("inf")
        for i in range(0,n,num):
            maxa = max(maxa,sum(dabba[i:i+num]))
            mina = min(mina,sum(dabba[i:i+num]))

        return maxa - mina
    ans = 0
    for i in range(1,int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans = max(run(i),ans)
            ans = max(run(n//i),ans)

    print(ans)