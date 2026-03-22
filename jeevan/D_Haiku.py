s1 = input()
s2 = input()
s3 = input()

ans = "YES"
s1v = 0
s2v = 0
s3v = 0

for i in s1:
    if i in "aeiou":
        s1v+=1
for i in s2:
    if i in "aeiou":
        s2v+=1
for i in s3:
    if i in "aeiou":
        s3v+=1

if s1v!=5 or s2v!=7 or s3v!=5:
    print("NO")

else:
    
    print("YES")