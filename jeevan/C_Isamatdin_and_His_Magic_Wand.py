t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    eve = sum(1 for i in arr if i%2)

    if eve == 0 or eve == n:
        print(*arr)
    else:
        print(*sorted(arr))