t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    sss = set(arr)
    for i in range(max(arr)+2):
        if i not in sss:
            print(i)
            break
