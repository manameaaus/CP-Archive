import math
# def front(lis,k):
#     c,r = 0,-1
#     count,sub = 0,0
#     for i in range(len(lis)-1):
#          
#             if lis[i] <= k:
#                 if count+1 == math.ceil((sub+1)/2):
#                     c += 1
#                     count,sub = 0,0
#                     r = i
#                 else:
#                     count += 1
#                     sub += 1
#             else:
#                 if c != 0 and i%2 == 1 and i == r+1:
#                     sub = sub
#                 else:
#                     sub += 1
#         else:
#             break

#     return [c,r]
import math
t =  int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    lis = l
    c,r = 0,-1
    count,sub = 0,0
    for i in range(len(lis)-1):
        if c < 2:
            if lis[i] <= k:
                if count+1 == math.ceil((sub+1)/2):
                    c += 1
                    count,sub = 0,0
                    r = i
                else:
                    count += 1
                    sub += 1
            else:
                if c != 0 and i%2 == 1 and i == r+1:
                    sub = sub
                else:
                    sub += 1
        else:
            break
    fronti = [c,r]

    lis = l[::-1]
    c,r = 0,-1
    count,sub = 0,0
    for i in range(len(lis)-1):
        if c < 2:
            if lis[i] <= k:
                if count+1 == math.ceil((sub+1)/2):
                    c += 1
                    count,sub = 0,0
                    r = i
                else:
                    count += 1
                    sub += 1
            else:
                if c != 0 and i%2 == 1 and i == r+1:
                    sub = sub
                else:
                    sub += 1
        else:
            break

    backi = [c,r]

    if fronti[0] == 2 or backi[0] == 2 or ((fronti[0] == 1 and backi[0] == 1) and (fronti[1] < n - (backi[1]+1) - 1)):
        print("YES")
    else:
        print("NO")