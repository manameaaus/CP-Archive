t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    ans = -1
    c = 0
    tom,rom = n,n
    while tom or rom:
        if tom == k or rom == k:
            ans = c
            break
        c+=1


        if tom == rom:
            tom , rom = tom//2 , tom - (tom // 2)
        else:
            temp = set()
            temp.add(tom // 2)
            temp.add(tom - tom//2)
            temp.add(rom // 2)
            temp.add(rom - rom//2)
            temp = sorted(temp)
            tom,rom = temp

        if c >= 100:
            break

    print(ans)
    