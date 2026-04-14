t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    s = set(l)
    print(2*len(s) - 1)