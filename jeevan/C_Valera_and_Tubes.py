n,m,k = map(int,input().split())
x = (n*m) + 2 - 2*k
c = 0
tot = n*m
maxa = x//m
if x>1:
    print(x,end=" ")
    flag = False
else :
    flag = True

for i in range(maxa):
    for j in range(m):
        if i % 2:
            print(i+1,m-j,end=" ")
        else:
            print(i+1,j+1,end=" ")
        tot -= 1

yo = x-maxa*m
i = maxa-1
if tot:
    if i % 2:
        if not flag:
            for j in range(yo):
                print(i+2,j+1,end=" ")
                lasy = j+1
            print()
        rem = m-yo
        
        if rem%2:
            
            for j in range(rem):
                print(2,i+2,j+1,i+3,j+1)

            for j in range(0,yo,2):
                print(2,i+3,j+1,i+3,j+2)

            for k in range(i+3,n,2):
                for j in range(m):
                    print(2,k+1,j+1,k+2,j+1)
        else:
            
            for j in range(yo,m,2):
                if flag and j==1:
                    print(3,i+2,j,i+2,j+1,i+2,j+2)
                    continue
                print(2,i+2,j+1,i+2,j+2)
           

            if (n-i-1)%2==1:
                for k in range(i+2,n,2):
                    for j in range(m):
                        print(2,k+1,j+1,k+2,j+1)
            else:
                for k in range(i+2,n):
                    for j in range(0,m,2):
                        print(2,k+1,j+1,k+1,j+2)

    else:
        
        
        for j in range(yo):
            print(i+2,m-j,end=" ")
            lasy = m-j
        print()
        rem = m-yo
        if rem%2:
            for j in range(m-yo):
                print(2,i+2,j+1,i+3,j+1)
            for j in range(m-yo,m,2):
                print(2,i+3,j+1,i+3,j+2)

            for k in range(i+3,n,2):
                for j in range(m):
                    print(2,k+1,j+1,k+2,j+1)
        else:
            for j in range(0,m-yo,2):
                print(2,i+2,j+1,i+2,j+2)
            if n%2==0:
                for k in range(i+2,n,2):
                    for j in range(m):
                        print(2,k+1,j+1,k+2,j+1)
            else:
                for k in range(i+2,n):
                    for j in range(0,m,2):
                        print(2,k+1,j+1,k+1,j+2)




        
# * * * *
# * * * *
# * * * *