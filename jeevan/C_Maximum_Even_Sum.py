t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    if a%2 and b%2:
        print(a*b+1)
    elif a%2 == 0 and b%2 == 1:
        print(-1)
    elif a%2 == 0 and b%2 == 0:
        print((a*(b//2) + 2))
    else:
        if b%4 == 0:
            print((a*(b//2) + 2))
        else:
            print(-1)



# 2 7
# 6 7
# 2 42


42

