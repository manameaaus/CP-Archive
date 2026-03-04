x,y = map(int,input().split())
j = min(x,y)
print(j+1)
for i in range(j+1):
    print(i,j-i)