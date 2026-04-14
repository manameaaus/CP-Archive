# t = int(input())
# for i in range(t):
#     n = int(input())
#     a = []
#     xx = {}
#     d = {}
#     for i in range(n):
#         l,r = map(int,input().split())
#         a.append([l,r])
#         if l==r:
#             if l in xx:
#                 xx[l]+=1
#             else:
#                 xx[l]=1
#     for i in a:
#         if i[0]==i[1]:
#             if xx[i[0]]>1:
#                 print("0",end="")
#             else:
#                 print("1",end="")
#         else:
#             for j in range(i[0],i[1]+1):
#                 if j not in xx:
#                     print("1",end="")
#                     break
#             else:
#                 print("0",end="")
#     print()

t = int(input())
for i in range(t):
    n = int(input())
    a = []
    xx = {}
    dy = set()
    dn = set()
    joker = []
    for i in range(n):
        l,r = map(int,input().split())
        a.append([l,r])
        if l==r:
            if l in xx:
                xx[l]+=1
            else:
                xx[l]=1
    for i in a:
        if i[0]==i[1]:
            if xx[i[0]]>1:
                print("0",end="")
            else:
                print("1",end="")
        else:
            for uuu in joker:
                if uuu<=i[1] and uuu>=i[0]:
                    print("1",end="")
                    break
            else:
                for j in range(i[0],i[1]+1):

                    if j not in xx:
                        joker.append(j)
                        print("1",end="")
                        break
                else:
                    print("0",end="")
    print()
