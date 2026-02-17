s = (input())
max = 0
c = 0
xx = s[0]
for i in range(len(s)):
    if s[i]==xx:
        c+=1
    else:
        xx=s[i]
        c=1
    if c>max:
        max=c
print(max)