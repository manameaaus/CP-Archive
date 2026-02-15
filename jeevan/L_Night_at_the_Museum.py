s = input()
s = "a"+s
x = 0
for i in range(len(s)-1):
    x += min(abs((ord(s[i])-ord(s[i+1]))),26-abs((ord(s[i+1])-ord(s[i]))))
print(x)