a,b,c,d = map(int,input().split())
kkk = 1 - ((b-a)*(d-c)/(b*d))
ddd = a / (b * kkk)
print(ddd)