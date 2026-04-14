# cook your dish here
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    a  = list(map(int,input().split()))
    b  = list(map(int,input().split()))
    
    mina = 0
    lisa_odd  = []
    lisa_even = []
    
    for i in range(n):
        mina += min(abs(a[i]-b[i]) , 9 - abs(a[i]-b[i]))
        lisa_odd.append(max(abs(a[i]-b[i]) , 9 - abs(a[i]-b[i])))
        
    
    if k == mina:
        print("YES")
    elif k < mina:
        print("NO")
    else:
        xxx = (k-mina)
        if xxx % 2 == 0:
            print("YES")
        else:
            lisa_odd.sort()
            if  (k - (mina - 9 + 2*lisa_odd[0]))  % 2 == 0 and (k - (mina - 9 + 2*lisa_odd[0])) >= 0:
                print("YES")
            else:
                print("NO")