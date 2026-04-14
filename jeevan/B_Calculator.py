s = input()
has = ""
c=0
for i in range(len(s)):
    if s[i] == "0" and s[i-1] == "0" and has:
        has = False
        continue
    elif s[i] == "0":
        has = True
        c+=1
    else:
        c+=1
print(c)