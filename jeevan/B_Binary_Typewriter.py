t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    c = 0
    new = ""
    curr = "0"
    for i in range(n):
        if s[i] != curr:
            new += curr
            c += 1
            curr = s[i]
    
    if c==0:
        print(n)
    elif c<3:
        print(n+1)
    else:
        print(n+c-2)

        
    



