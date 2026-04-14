po = [1]
for i in range(1, 63) :
    po.append(4 * po[-1])
def where_num(d,n):
    if n == 0:
        return
    pot = po[n-1]
    l = [pot*1,pot*2,pot*3,pot*4]
    step = 2**(n-1)

    if d<=l[0]:
        ans["x"] += 0
        ans["y"] += 0
        d -= 0
    elif d<=l[1]:
        ans["x"] += step
        ans["y"] += step
        d -= l[0]
    elif d<=l[2]:
        ans["x"] += 0
        ans["y"] += step
        d -= l[1]
    else:
        ans["x"] += step
        ans["y"] += 0
        d -= l[2]

    where_num(d,n-1)



def what_num(x,y,n):
    if n == 0 :
        return 1
    xxx = nini[n-1]

    pot = po[n-1]

    if x<=xxx and y<=xxx:
        return what_num(x,y,n-1)
    elif x>xxx and y<=xxx:
        return what_num(x-xxx,y,n-1) + pot*3
    elif x<=xxx and y>xxx:
        return what_num(x,y-xxx,n-1) + pot*2
    else:
        return what_num(x-xxx,y-xxx,n-1) + pot

# nini  = [2**i for i in range(62)]
 
# print(what_num(7,6,50))
t = int(input())
# t = 0

for i in range(t):
    n = int(input())
    q = int(input())
    power = [2**(2*i) for i in range(31)]
    nini  = [2**i for i in range(62)]
    for i in range(q):
        s = input().split()
        if s[0] == "->":
            x = int(s[1])
            y = int(s[2])
            to = max(x,y)
            for i in range(31):
                if nini[i] >= to:
                    xxxx = i + 1
                    break

            # print(nini[i])
            print(int(what_num(y,x,xxxx)))
        else:
            ans = {"x":1,"y":1}
            for i in range(31):
                if power[i] >= int(s[1]):
                    uuu = i+1
                    break
            where_num(int(s[1]),uuu)
            print(ans["y"],ans["x"])



    


# ans = {"x":1,"y":1}
# where_num(47,3)

# where_num(64,3)
# print(ans)
    

# print(what_num(8,1,3))  # 1+2+4+



# print(what_num(6,7,60))
# print(what_num(80743665,9880055,61))
# 
# print(ans)

# (where_num(13635218194978088,28))
# print(ans)
# ans = {"x":1,"y":1}
# (where_num(9114113617909047,28))
# print(ans)



