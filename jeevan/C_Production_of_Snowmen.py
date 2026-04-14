t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    count1 = 0
    count2 = 0
    for st in range(n):
        for i in range(n):
            if a[(st+i) % n] >= b[i]:
                break
        else:
            count1 += 1


        for i in range(n):
            if c[(st+i) % n] <= b[i]:
                break
        else:
            count2 += 1

        
    print(n * count1 * count2)