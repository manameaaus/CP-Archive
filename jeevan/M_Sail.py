no,x1,y1,x2,y2 = map(int,input().split())
se = input()

if y2 - y1 > 0 :
    n = y2 - y1
    s = 0
else:
    s = y1 - y2
    n =0


if x2 - x1 > 0:
    e = x2 - x1
    w = 0
else:
    w = x1 - x2
    e = 0

gs,gn,gw,ge = 0,0,0,0
# print(n,s,e,w)
t = 0
while t<len(se):
    if se[t] == "N":
        gn += 1
    elif se[t] == "S":
        gs += 1
    elif se[t] == "E":
        ge += 1
    elif se[t] == "W":
        gw += 1
    if gn>=n and gs>=s and ge>=e and gw>=w:
        print(t+1)
        break
    t += 1
else:
    print(-1)   


# if gn<n and gs<s and gw<w and ge<e:
#     print(-1)
# else:
#     print(t)

# print(gn,gs,ge,gw)



