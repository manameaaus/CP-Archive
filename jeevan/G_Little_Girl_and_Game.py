s = input()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
oddc = sum(1 for i in d if d[i] % 2 != 0)

if oddc==0:
    print("First")
else:
    if oddc%2:
        print("First")
    else:
        print("Second")

