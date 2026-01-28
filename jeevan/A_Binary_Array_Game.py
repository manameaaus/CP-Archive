t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    if l[0] == 1 or l[-1] == 1:
        print("Alice")
    else:
        print("Bob")