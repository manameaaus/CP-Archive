n , h = map(int,input().split())
a = list(map(int,input().split()))
c = 0
for i in a:
    if i>h:
        c+=1
print(n+c)