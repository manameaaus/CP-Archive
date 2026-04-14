t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    odd = []
    even = []
    for i in range(n):
        if i % 2:
            odd.append(l[i])
        else:
            even.append(l[i])
    odd.sort()
    even.sort()
    new = [0] * n
    x = 0
    for i in range(0,n,2):
        new[i] = even[x]
        x += 1
    x = 0
    for i in range(1,n,2):
        new[i] = odd[x]
        x += 1

    extra = [0] * (n+1)
    for i in range(n):
        extra[l[i]] = i
    def swap(i,ind_expect):
        l[i],l[i+1],l[ind_expect],l[ind_expect+1],extra[l[ind_expect]],extra[l[ind_expect+1]],extra[l[i]],extra[l[i+1]] = l[ind_expect],l[ind_expect+1],l[i],l[i+1],ind_expect,ind_expect+1,i,i+1


    for i in range(n-3):
        ind_expect = extra[new[i]]
        if ind_expect < n-1:
            swap(i,ind_expect)
        else:
            swap(n-4,n-2)
            swap(i,n-3)

    print(*l)
