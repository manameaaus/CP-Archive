n = int(input())
l = list(map(int,input().split()))
d = {}
for i in range(n):
    if l[i] in d:
        d[l[i]].append(i)
    else:
        d[l[i]] = [i]

# print(d)
ans = 0
pot = []
for i in d:
    got = d[i]
    if len(got) > 2:
        diff = got[1] - got[0]
        for j in range(1,len(got)):
            if got[j] - got[j-1] != diff:
                break
        else:
            ans += 1
            pot.append([i,diff])
    else:
        if len(got) == 2:
            diff = got[1] - got[0]
            ans+=1
            pot.append([i,diff])
        else:
            ans+=1
            pot.append([i,0])


print(ans)
pot.sort()
for i in pot:
    print(*i)



