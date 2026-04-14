t = int(input())
lis = []
for j in range(1,400*3,3):
    for i in range(1,400*3,3):
        lis.append([i+j,i,j,True])
        lis.append([i+j+1,i+1,j,False])
for i in range(1,400*3,3):
    for j in range(2,400*3,3):
        lis.append([i+j,i,j,False])
        lis.append([i+j+3,i+1,j,False])
lis.sort()
x = len(lis)
fresh = []
for i in range(x):
    if lis[i][3]:
        fresh.append([[lis[i][1],lis[i][2]],i])


for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ttrrtt = fresh[n][1]
    don = [1] * (ttrrtt+n)
    curr = 0
    zom = 0
    for i in a:
        if i:
            while don[curr] == 0:
                curr += 1
            print(lis[curr][1],lis[curr][2])
            don[curr] = 0
            curr += 1
        else:
            while don[fresh[zom][1]] == 0:
                zom += 1
            fk = fresh[zom]
            print(fk[0][0],fk[0][1])
            don[fk[1]] = 0
            zom += 1




            



# [[2, 1, 1, True], 
#  [3, 1, 2, False], 
#  [3, 2, 1, False], 
#  [5, 1, 4, True], 
#  [5, 4, 1, True], 
#  [6, 1, 5, False], 
#  [6, 2, 2, False], 
#  [6, 2, 4, False], 
#  [6, 4, 2, False], 
#  [6, 5, 1, False], 
#  [8, 1, 7, True], 
#  [8, 4, 4, True], 
#  [8, 7, 1, True], 
#  [9, 1, 8, False], 
#  [9, 2, 5, False], 
#  [9, 2, 7, False]]



# print(fresh[25425])
# print(len(lis))
# print(lis[101473:101477])
# [[675, 673, 2, False], [675, 674, 1, False], [677, 4, 673, True], [677, 7, 670, True]]

# [[[661, 13], 100796], 
# [[664, 10], 100797], 
# [[667, 7], 100798], 
# [[670, 4], 100799], 
# [[673, 1], 100800], 
# [[4, 673], 101475], 
# [[7, 670], 101476], 
# [[10, 667], 101477], 
# [[13, 664], 101478], 
# [[16, 661], 101479]]

