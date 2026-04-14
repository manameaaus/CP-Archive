# t = int(input())
# for i in range(t):
#     n = int(input())
#     arr = list(map(int,input().split()))


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()


    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    curr = d.get(0,0)

    chance = 0
    
    for i in range(max(arr) + 1):
        if d.get(i,0) == 0:
            print(i)
            break
        elif d[i] == 1:
            if chance == 1:
                print(i)
                break
            else:
                chance = 1
    else:
        print(max(arr) + 1)




    # ans = max(arr) + 1

    # if not curr:
    #     ans = 0
    # else:
    #     for i in range(1,max(arr) + 1):
    #         if d[i] <= curr:
    #             ans = i
    #             # print("hello",i,curr)
    #             break
    #         else:
    #             curr += d[i]

    # print(ans)

    # mex = 0

    # end = -1
    # for i in range(n):
    #     if arr[i] == mex:
    #         mex += 1
            
    #     elif arr[i] > mex:
    #         break

    #     end = i



    # ans = mex

    # st = 0
    # curr = arr[0]
    # c = 1

    # while st < n:
    #     if curr != arr[st]:
    #         if c == 1:
    #             ans = min(ans,curr)
    #             break
    #         else:
    #             curr = arr[st]
    #             c = 1
    #     else:
    #         c += 1
    #     st += 1

    # if c == 1:
    #    ans = min(ans,curr) 


    # print(ans)

    # # print(mex,end)
    # d = {}

    # maxa = -1

    # win = [0] * (mex+2)
    # for i in range(end+1):
    #     if arr[i] in d:
    #         d[arr[i]] += 1
    #         win[arr[i]] = 0
    #     else:
    #         d[arr[i]] = 1
    #         win[arr[i]] = 1
    #     maxa = max(maxa,arr[i])
    #     # print(maxa,arr[i])

    # ans = maxa + 1
    # # print(ans)
    # # print(win)
    # # print(d)
    # for i in range(1,len(win)):
    #     if win[i]:
    #         ans = i
    #         break

    # # if d[0] == 1:

    # print(ans)

