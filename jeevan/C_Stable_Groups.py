n,k,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

ade_tade = 0
l = []

for i in range(1,n):
    ddd = a[i] - a[i-1]
    if ddd > x:
        ade_tade += 1
        l.append((ddd-1)//x)

maxa = 0
l.sort()
# print(l)
jotty = len(l)
i = 0
j = 0
curr = 0
while i <= j and j<len(l):
    # curr + l[i]
    if curr + l[j] <= k:
        curr += l[j]
        maxa = max(maxa,j-i+1)
        j += 1

    else:
        curr -= l[i]
        i += 1

jotty -= maxa
print(jotty+1)


# 0 1 2 3 4 5 6 7 
# 3 4 5 6 7 8 9 0