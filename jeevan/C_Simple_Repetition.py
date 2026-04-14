t = int(input())
for i in range(t):
    x,k = map(int,input().split())
    if x > 1:
        if k>1:
            print("NO")
        else:
            for i in range(2,int(x**(0.5))+1):
                if x%i==0:
                    print("NO")
                    break
            else:
                print("YES")
        
    else:
        if k == 2:
            print("YES")
        else:
            print("NO")