n = int(input())
a = list(map(int,input().split()))
oddi = -1
eveni = -1
oddc = 0
evec = 0
for i in range(n):
    if a[i]%2 == 1:
        oddc+=1
        if oddi ==-1:
            oddi = i
    else:
        evec+=1
        if eveni ==-1:
            eveni = i
    if (oddc==1 and evec>1) or (evec==1 and oddc>1):
        break
if oddc==1:
    print(oddi+1)
elif evec==1:
    print(eveni+1)
