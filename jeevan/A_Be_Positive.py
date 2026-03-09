t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))

    k = l.count(-1)

    

    print(((k%2) * 2) + l.count(0))