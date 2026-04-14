MAXN = 100002
spf = [i for i in range(MAXN)]
color = [1] * MAXN
for i in range(2,MAXN):
    if spf[i] == i:
        for j in range(i*i,MAXN,i):
            spf[j] = min(spf[j],i)
            if spf[j] == i:
                color[j] = 2

n = int(input())
print(max(color[2:n+2]))
print(*(color[2:n+2]))



