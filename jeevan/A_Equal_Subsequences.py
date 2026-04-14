t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    new = ["0"] * (n)
    for i in range(n-k,n):
        new[i] = "1"
    print("".join(new))
    
