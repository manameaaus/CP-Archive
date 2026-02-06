n = int(input())
l = list(map(int,input().split()))

curr = 0
maxa = -1000

for i in l:
    if i == 0:
        curr += 1
    else:
        curr -= 1
    maxa = max(maxa,curr)
    curr = max(0,curr)

print(l.count(1)+maxa)


