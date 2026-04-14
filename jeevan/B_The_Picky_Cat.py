t = int(input())
for i in range(t):
    n = int(input())
    l = [abs(i) for i in map(int,input().split())]
    tarpos = l[0]
    l.sort()
    less = l.index(tarpos)

    if n%2 == 0:
        exp_low = n//2-1
    else:
        exp_low = n//2
    
    if (less <= exp_low):
        print("YES")
    else:
        bigger = n-1-less
        if bigger >= exp_low:
            print("YES")
        else:
            print("NO")

        




