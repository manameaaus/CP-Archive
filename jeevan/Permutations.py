n = int(input())
if n==1:
    print(1)
elif n<4:
    print("NO SOLUTION")
elif n==4:
    print("2 4 1 3")
else:
    if n%2==0:
        x=n//2
    else:
        x=n//2+1
    for i in range(1,x):
        print(i,i+x,end=" ")
    if n%2==0:
        print(n//2,n//2*2,sep=" ")
    else:
        print(n//2+1)
