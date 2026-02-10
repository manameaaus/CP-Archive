# t = int(input())
# for i in range(t):
#     n,k = map(int,input().split())
#     s = input()
#     if n == 1 or (k == 0 and s[0] >= s[-1]) or (s.count(s[0]) == n):
#         print("NO")
#     else:
#         print("YES")


t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    s = input()
    if n == 1:
        print("NO")
    elif (k == 0 and s >= s[::-1]):
        print("NO")
    elif (s.count(s[0]) == n):
        print("NO")
    else:
        print("YES")