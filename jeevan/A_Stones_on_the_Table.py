n = int(input())
s = input()
c = 1
y = 0
for i in range(1,n):
    if s[i] == s[i-1]:
        c += 1
    else:
        y+=c-1
        c = 1
y+=c-1
print(y)
