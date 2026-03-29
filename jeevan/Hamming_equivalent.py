t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    def  countSetBits(n):
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count
    xx = [countSetBits(i) for i in range(1,n+1)]
    bb = [countSetBits(i) for i in a]

    if xx==bb:
        print("YES")
    else:
        print("NO")