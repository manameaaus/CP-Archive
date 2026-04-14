t = int(input())
for i in range(t):
    n,k = input().split()
    n = int(n)
    s = input()
    j = s.count(k)
    if j == n:
        print(0)
    elif s[-1] == k:
        print(1)
        print(n)
    else:
        if s[-2] == k:
            print(1)
            print(n-1)
        else:
            for i in range(n-1,-1,-1):
                if s[i] == k:
                    if (i+1) * 2 > n:
                        print(1)
                        print((i+1))
                        break
            else:
                print(2)
                print(n,n-1)


        # else:
        #     print(2)
        #     print(n,n-1)