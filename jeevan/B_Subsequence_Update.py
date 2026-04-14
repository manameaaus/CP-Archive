t = int(input())
for i in range(t):
    n,l,r = map(int,input().split())
    arr = list(map(int,input().split()))
    print(min(sum(sorted(arr[:r])[:r-l+1]),sum(sorted(arr[l-1:])[:r-l+1])))
