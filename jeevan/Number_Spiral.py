'''
1  2  9  10 25 26
4  3  8  11 24 27
5  6  7  12 23 28
16 15 14 13 22 29
17 18 19 20 21 30
36 35 34 33 32 31
'''

t = int(input())
for i in range(t):
    r,c = map(int,input().split())
    if r%2==0:
        if c>r:
            if c%2==1:
                print(int(c**2-r+1))
            else:
                print(int((c-1)**2+1+r-1))
        else:
            print(r**2-c+1)
    else:
        if c>r:
            if c%2==1:
                print(int(c**2-r+1))
            else:
                print(int((c-1)**2+1+r-1))
        else:
            print(((r-1)**2)+c)


