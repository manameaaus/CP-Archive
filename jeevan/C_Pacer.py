t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    curr_time = 0
    ans = 0
    side = 0

    for i in range(n):
        a,b = map(int,input().split())
        sec = a-curr_time
        if side == b:
            ans += sec - sec%2
        else:
            ans += sec - (sec+1) % 2
        side = b
        curr_time = a

    if curr_time < m:
        ans += m-curr_time

    print(ans)