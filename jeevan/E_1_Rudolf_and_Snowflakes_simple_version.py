valid = set()
for i in range(2,1001):
    st = i + 1
    curr = i
    while st <= 1000000:
        curr *= i
        st += curr
        valid.add(st)
    

t = int(input())
for i in range(t):
    n = int(input())
    if n in valid:
        print("YES")
    else:
        print("NO")
