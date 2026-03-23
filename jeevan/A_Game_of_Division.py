t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))

    freq = [0] * k
    for i in l:
        freq[i%k] += 1

    for i in range(k):
        if freq[i] == 1:
            print("YES")
            for j in range(n):
                if l[j] % k == i:
                    print(j+1)
                    break
            break
    else:
        print("NO")

            
                