x = int(input())
l = [16]
c = x
tempo  = 0
for i in range(2,int(x**(0.5))+1):
    c += (x//i)*i
    l.append((x//i))
    
for i in range(len(l)-1):
    c += (l[i]-l[i+1])*i+1
print(l)
print(c%(10**9+7))


