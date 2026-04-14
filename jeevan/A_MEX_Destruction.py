t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    joke =  0
    found = False 
    for j in range(n):
        if a[j] == 0 and joke==0:
            joke=1
            found = True

        # elif a[j] == 0 and joke==0
            
