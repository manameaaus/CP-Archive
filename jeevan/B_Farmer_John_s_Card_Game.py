t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    lis = []
    tempo = [0]*n
    for i in range(n):
        row = list(map(int,input().split()))
        row.sort()
        lis.append(row)
        tempo[i] = row[0]
    
    
    for i in range(n):
        if i in tempo:
            continue
        print(-1)
        break

    else:
        permu = [0]*n
        ans = True
        for i in range(n):
            if ans:
                ini = lis[i][0]
                permu[ini] = i+1
                for j in range(m):
                    if lis[i][j]%n != ini:
                        ans = False
                        print(-1)
                        break
            else:
                break
            
        else:
            print(*permu)
            

        