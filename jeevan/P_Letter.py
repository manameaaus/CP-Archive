s1 = input()
s2 = input()

d1 = {}
d2 = {}

for i in s1:
    if i!=" ":
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1

for i in s2:
    if i!=" ":
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1


for i in d2:
    if d1.get(i,0) < d2[i]:
        print("NO")
        break
else:
    print("YES") 
