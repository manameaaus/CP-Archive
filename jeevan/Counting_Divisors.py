t = int(input())
l = []
for i in range(t):
    l.append(int(input()))

x = max(l)

jj = [0]*(x+1)
jj[0] = 1
jj[1] = 0

for i in range(1,x+1):
    for j in range(i,x+1,i):
        jj[j] += 1

for i in l:
    print(jj[i])
