import math
def is_prime(n):
    checktill=int(math.sqrt(n))
    if n<=1:
        return False
    is_prime=True
    for i in range(2,checktill+1):
        if n%i==0:
            is_prime=False
            break
    return is_prime

n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    z=math.sqrt(l[i])
    if int(z)-z==0:
        if is_prime(int(z)):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")