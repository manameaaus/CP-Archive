t = int(input())
for i in range(t):
    n,k,p = map(int,input().split())
    a = list(map(int,input().split()))
    if k+max(a) > sum(a)-max(a)+p:
        print("Ved")
    elif k+max(a) == sum(a)-max(a)+p:
        print("Equal")
    else:
        print("Varun")