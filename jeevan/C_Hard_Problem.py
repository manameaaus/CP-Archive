t = int(input())
for i in  range(t):
    m,a,b,c = map(int,input().split())
    co = 0
    co+=min(a,m)
    co+=min(b,m)
    rem = 0 
    if a<m:
        rem += m-a
    if b<m:
        rem += m-b
    co+=min(c,rem)
    print(co)