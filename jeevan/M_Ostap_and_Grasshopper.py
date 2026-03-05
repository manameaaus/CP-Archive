n , k = map(int,input().split())
s = input()
xx = min(s.index("T"),s.index("G"))
d = s[xx:]
j = ""
if xx==s.index("G"):
    d = s[xx:]
    for i in range(0,len(d),k):
        
        if d[i]=="G" or d[i]=="T" or d[i]=="#":
            j+=d[i]
        if j=="GT":
            break
else:
    d = s[:s.index("G")+1]
    for i in range(len(d)-1,-1,-k):

        if d[i]=="G" or d[i]=="T" or d[i]=="#":
            j+=d[i]
        if j=="GT":
            break

if j=="GT" or j=="TG":
    print("YES")
    
else:
    print("NO")
    