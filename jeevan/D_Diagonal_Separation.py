n,m = map(int,input().split())
dc = {"W":{},"B":{}}
dr = {"W":{},"B":{}}
for i in range(m):
    r,c,p = (input().split())
    r = int(r)
    c = int(c)
    if c in dc:
        if p in dc[c]:
            dc[c][p].append(r)
        else:
            dc[c][p] = [r]
    else:
        dc[c][p] = [r]
    
