t = int(input())
for i in range(t):
    n,r,b = map(int,input().split())

    if b >= r:
        if n%2 == b%2:
            print("YES")
        else:
            print("NO")
    elif r > b:
        if n%2 == b%2 == r%2:
            print("YES")
        else:
            print("NO")
