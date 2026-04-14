l = []
for i in range(1,6):
    a = list(map(int,input().split()))
    for j in range(5):
        if a[j]==1:
            print(abs(3-i)+abs(2-j))
            break