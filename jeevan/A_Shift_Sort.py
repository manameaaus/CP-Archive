t = int(input())
for i in range(t):
    s = int(input())
    n = input()
    
    zero = n.count("0")
    

    c = 0
    for i in range(zero):
        if n[i] == "0":
            c += 1

    

    print(zero-c)

