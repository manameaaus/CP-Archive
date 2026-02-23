n = int(input())
s = input()
a = s.count("A")
d = s.count("D")
if d>a:
    print("Danik")
elif a>d:
    print("Anton")
else:
    print("Friendship")
