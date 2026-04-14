a = list(map(int,input().split()))
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
if ((3 in d.values()) and (1 in d.values())) or ((2 in d.values()) and len(d)==2):
    print("Yes")
else:
    print("No")