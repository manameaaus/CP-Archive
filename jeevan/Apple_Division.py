# n = int(input())
# l = sorted(list(map(int,input().split())))
# x = sum(l)
# xx = x//2
# c = 0
# for i in range(n-1,-1,-1):
#     if c+l[i]<=xx:
#         c+=l[i]
# print(c)
# print(x-2*c)

def solve(a,x,c):
    global xox,poker
    if x<=0:
        poker = min(poker,abs(xox-(2*c)))
        return
    if a==[]:
        return
    solve(a[1:],x-a[0],c+a[0])
    solve(a[1:],x,c)



n = int(input())
l = sorted(list(map(int,input().split())))[::-1]
xox = sum(l)
poker = xox
solve(l,xox//2,0)
print(poker)

# def solve(a,x,c):
#     global xox
#     if x<=0:
#         return abs(xox-(2*c))
#     if a==[]:
#         return float("inf")
#     c = solve(a[1:],x-a[0],c+a[0])
#     d = solve(a[1:],x,c)
#     return min(c,d)



# n = int(input())
# l = sorted(list(map(int,input().split())))[::-1]
# xox = sum(l)
# print(solve(l,xox//2,0))
