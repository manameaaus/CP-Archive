import math
def f(n,l,m):
    return (n//l) * m + min(m-1,n%l)


t = int(input())
for i in range(t):
    a,b,q = map(int,input().split())
    lcm = math.lcm(a,b)
    a , b = min(a,b),max(a,b)
    m = max(a,b)
    for i in range(q):
        l,r = map(int,input().split())
        print((r-l+1) - (f(r,lcm,m) - f(l-1,lcm,m)),end = " ")
    print()



# for i in range(1,201):
#     print(i % 7, end= " ")
# print()
# for i in range(1,201):
#     print(i%10,end = " ")
# print()
# for 