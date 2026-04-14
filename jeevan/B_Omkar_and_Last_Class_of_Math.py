import math 
t = int(input())
for i in range(t):
    n = int(input())
    maxa = 1
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            maxa = max(maxa,i)
            maxa = max(maxa,n//i)

    print(maxa,n-maxa)
