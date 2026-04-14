n = int(input())
pri = []
sec = []
for i in range(n):
    f,s = map(int,input().split())
    pri.append(f)
    sec.append(s)


ans = 0

f = sum(pri)
s = sum(sec)

for i in range(n):
    ans += max(pri[i] - s + sec[i],0)
    pri[i] = min(pri[i],s - sec[i])

# print(pri)
# print(sec)
# print()

f = sum(pri)
for i in range(n):
    ans += max(sec[i] - f + pri[i],0)
    sec[i] = min(sec[i],f - pri[i])


# print(pri)
# print(sec)


print(abs(sum(pri)-sum(sec)) + ans)
# print(abs(sum(pri)-sum(sec)))
