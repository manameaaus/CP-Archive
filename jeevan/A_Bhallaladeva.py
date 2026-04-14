n = int(input())
l = list(map(int,input().split()))
l.sort()
pre = [0] * (n+1)
for i in range(n):
    pre[i+1] = pre[i] + l[i]
q = int(input())
for i in range(q):
    k = int(input()) + 1
    print(pre[(n + k - 1) // k])