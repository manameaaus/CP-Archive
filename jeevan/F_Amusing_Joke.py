s1 = input()
s2 = input()
pile = input()
j = s1+s2

if len(j)==len(pile):
    d1={}
    d2={}
    for i in j:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    for i in pile:
        if i in d2:
            d2[i]+=1
        else:
            d2[i]=1
    if d1==d2:
        print("YES")
    else:
        print("NO")

else:
    print("NO")