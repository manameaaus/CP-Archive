def prin(n):
    if n == 0:
        return
    
    prin(n-1)
    print(n)

n = int(input())
prin(n)