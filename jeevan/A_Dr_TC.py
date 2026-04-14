t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    print(((s.count("1") + 1) * s.count("0")) + ((s.count("1") - 1) * s.count("1")))