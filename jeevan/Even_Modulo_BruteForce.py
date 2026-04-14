v = list(map(int,input().split()))

for i in range(len(v)):
    for j in range(i+1,len(v)):
        print(i, j, j%i)