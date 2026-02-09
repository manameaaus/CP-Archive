n = int(input())
a = list(map(int,input().split()))
if sum(a)%n == 0:
    print(n)
else:
    print(n-1)