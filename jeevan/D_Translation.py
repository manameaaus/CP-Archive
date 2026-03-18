# A B C D E F G H I J K L M N O Q R S T U V W X Y Z
# n 0 U 0 Z 0 0 b v z I 0 s 0 u 0 i l N S V 0 t e c
# P 0 E 0 0 Y a W 0 0 0 D A m x q F L 0 p C 0 B o 0
# a b c d e f g h i j k l m n o q r s t u v w x y z


s = input()
t = input()
d = {}
for i in range(len(s)):
    d[t[i]] = s[i]
s = set()
se = set()
ll = sorted(d.items())

for i in d:
    if d[i] in s:
        print(d[i]) 
        break
    if i in se:
        print(i)
        break
    s.add(d[i])
    se.add(i)
print(ll)
print(len(ll))
