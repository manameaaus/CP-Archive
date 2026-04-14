t = int(input())
for i in range(t):
    n, x = map(int, input().split())    
    temp = 0
    for i in range(n - 1):
        if x < x|i:
            for j in range(n-1-i):
                print(max(0,i-1), end=" ")
            break
        else:
            print(i, end=" ")
        temp |= i 
    if (temp | (n - 1)) == x:
        print(n - 1)
    else:
        print(x)
