t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = sum(1 for i in a if i%2==0)
    y = n-x
    if x>0:
        print(y+1)
    else:
        print(y-1)