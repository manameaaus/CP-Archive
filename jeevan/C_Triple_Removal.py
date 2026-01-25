t = int(input())
for i in range(t):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))

    pre_z = [0] * (n+1)
    pre_o = [0] * (n+1)
    pre_dz = [0] * (n+1)
    pre_do = [0] * (n+1)


    c_zero = 0
    c_one = 0

    c_dz = 0
    c_do = 0


    for i in range(n):
        if arr[i] == 0:
            c_zero += 1
            if i > 0:
                if arr[i-1] == 0:
                    c_dz += 1
        else:
            c_one += 1
            if i > 0:
                if arr[i-1] == 1:
                    c_do += 1

        pre_z[i+1] = c_zero
        pre_o[i+1] = c_one
        pre_dz[i+1] = c_dz
        pre_do[i+1] = c_do



    for i in range(q):
        l,r = map(int,input().split())
        c_zero = pre_z[r] - pre_z[l-1]
        c_one = pre_o[r] - pre_o[l-1]

        if (c_one % 3 == 0) and (c_zero % 3 == 0):
            if (pre_dz[r] - pre_dz[l]) or (pre_do[r] - pre_do[l]):
                print((c_zero//3) + (c_one//3))
            else:
                print((c_zero//3) + (c_one//3) + 1)
        else:
            print(-1)




    