n = int(input())
l = list(map(int,input().split()))
c = 0
while l!=sorted(l):
    for i in range(n-1):
        if l[i]>l[i+1]:
            c+=l[i]-l[i+1]
            l[i+1]=l[i]

print(c)