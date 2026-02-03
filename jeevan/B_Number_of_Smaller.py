n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


i = 0
j = 0
c = 0
co = [-1] * (m)
while i<n and j<m:
    if a[i] < b[j]:
        c += 1
        i = i+1
    else:
        co[j] = c
        j+=1


for l in co:
    if l==-1:
        print(n,end = ' ')
    else:
        print(l,end=" ")

