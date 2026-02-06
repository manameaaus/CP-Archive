# t = int(input())
# for i in range(t):
#     n = int(input())
#     row1 = list(map(int,input().split()))
#     row2 = list(map(int,input().split()))
    
#     sumrow = [row1[i]+row2[i] for i in range(n)]
#     sdo = sumrow.index(max(sumrow)) 
#     c = row1[sdo]+row2[sdo]
#     maxrow = {}
#     for i in range(n):
#         if row1[i] > row2[i]:
#             maxrow[i] = 1
#         elif row1[i] < row2[i]:
#             maxrow[i] = 2
#         else:
#             maxrow[i] = 0
#     l = []
#     for k,v in maxrow.items():
#         l.append([v,k])
#     l.sort()
#     for i in range(n):
#         if l[i][1]!=sdo:
#             if l[i][0] == 1:
#                 if row1[l[i][1]]>0:
#                   c+=row1[l[i][1]]
#             elif l[i][0] == 2:
#                 if row2[l[i][1]]>0:
#                     c+=row2[l[i][1]]
#             else:
#                 if row1[l[i][1]]>0:
#                    c+=row2[l[i][1]]
#     print(c)
            
t = int(input())
for i in range(t):
    n = int(input())
    row1 = list(map(int,input().split()))
    row2 = list(map(int,input().split()))
    c = 0
    j = -10000000000000000000000
    for i in range(n):
        c+=max(row1[i],row2[i])
        if min(row1[i],row2[i])>j:
            j = min(row1[i],row2[i])
    print(c+j)

    # l = []
    # for k,v in maxrow.items():
    #     l.append([v,k])
    # l.sort()
    # for i in range(n):
    #     if l[i][1]!=sdo:
    #         if l[i][0] == 1:
    #             c+=row1[l[i][1]]
    #         elif l[i][0] == 2:
    #             c+=row2[l[i][1]]
    #         else:
    #             c+=row2[l[i][1]]
            


