t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    curr = 1
    print(1,end = " ")
    for i in range(1,n):
        if a[i - curr] >= curr+1:
            curr += 1
        print(curr,end = " ")

    print()

        