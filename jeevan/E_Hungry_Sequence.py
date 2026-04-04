def seive(n):
    l = [True]*(n+1)
    l[0] = l[1] = False
    for i in range(2, int(n**0.5)+1):
        if l[i]:
            for j in range(i*i,n+1,i):
                l[j] = False
    return l
x = seive(10000000)
n = int(input())
for i in range(10000000+1):
    if x[i]:
        print(i,end=" ")
        n -= 1
    if n==0:
        break


