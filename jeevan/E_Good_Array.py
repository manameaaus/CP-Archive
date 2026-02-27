n =  int(input())
a = list(map(int,input().split()))

d = {}
for i in range(n):
    if a[i] in d:
        d[a[i]].append(i+1)
    else:
        d[a[i]] = [i+1]
l  = []
suma = sum(a)
for i in a:

    if suma - (2*i) in d:
        got = d.get(suma - (2*i),[])
        if suma - (2*i) != i:
            
            l.extend(got)
        elif len(got) > 1:
            l.extend(got)

l = set(l)
print(len(l))
if len(l):
    print(*l)

