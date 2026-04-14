n = int(input())
i = 5
c = 0
while n>0 and i>0:
    c = c + n//i
    n%=i
    i-=1
print(c)
