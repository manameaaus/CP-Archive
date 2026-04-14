t = int(input())
for i in range(t):
    w,h,a,b = map(int,input().split())
    x1,y1,x2,y2 = map(int,input().split())
    
    if((abs(x1-x2) != 0 and abs(x1-x2) % a == 0) or (abs(y1-y2) != 0 and abs(y1-y2) % b == 0)):
        print("Yes")
    else:
        print("No")