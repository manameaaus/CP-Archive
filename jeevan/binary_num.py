n = int(input())
lis=[]
for i in range(2**n):
    b = ((bin(i).split('0b')[1]))
    sss = len(str(b))
    lis.append("0"*(n-sss)+b)
for i in lis:
    print(i)