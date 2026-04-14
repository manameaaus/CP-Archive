t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    left = [0] * n
    for j in range(1,n):
        left[j] = abs(l[j-1] - l[j])

 
    res = [0] * n
    r = [0] * n

    curr = [[0,0]]
    for i in range(1,n):
        while curr and  left[i] < curr[-1][0]:
            curr.pop()

        if curr:
            r[i] += i - curr[-1][1]
        curr.append([left[i],i])


    curr = [[0,n]]
    for i in range(n-1,0,-1):
        while curr and  left[i] <= curr[-1][0]:
            curr.pop()

        if curr:
            r[i] *= curr[-1][1] - i
            res[left[i]] += r[i]
        
        curr.append([left[i],i])



    for i in range(n-2,-1,-1):
        res[i] += res[i+1]

    print(*res[1:])


        



        
            


    # print(left)

    


# 3 1 2 4
# 0 2 1 2


# 5 1 4 2 3
# 0 4 3 2 1 -> l
# 4 3 2 1 0 -> r

# 3 1 2 4
# 0 2 1 2


# 1 2 3 4 5
# 0 1 1 1 1

# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 2 3
# 2 3 4
# 2 3 4 5

# 3 4
# 3 4 5

# 4 5