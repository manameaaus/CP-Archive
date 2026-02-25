t = int(input())
#  n-i+1 ind 1 based
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if l[1] % 2 and n-1 % 2 == 0:
        print("NO")
    else:
        p = l[0]
        q = l[1]

        b = (2*p - q) / (n+1)
        a = p - (n * b)
        if b != int(b) or a != int(a) or b < 0 or a < 0: 
            print("NO")
        else:
            a = p - (n * b)
            for i in range(n):
                x = i+1
                y = n-i
                if (a * x) + (b * y) != l[i]:
                    print("NO")
                    break
            else:
                print("YES")  

