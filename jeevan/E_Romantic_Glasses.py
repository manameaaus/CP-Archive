t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    to_use = [l[i] if i%2 == 0 else -l[i] for i in range(n)]
    prefix_sums = set()
    prefix_sums.add(0)
    curr = 0
    for num in to_use:
        curr += num
        if curr in prefix_sums:
            print("YES")
            break
        prefix_sums.add(curr)
    else:
        print("NO")

    
