from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    dabba = list(input().split())
    s = list(dabba[0])
    t = list(dabba[1])
    if Counter(s) == Counter(t):
        print("YES")
    else:
        print("NO")