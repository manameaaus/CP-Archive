# s  = "-39, 26, -45, 19, -97, 49, -7, 18"
# s = "49, -24, 56"
# arr = list(map(int,s.split(", ")))
# doctor = sum(arr)

# s = "-55, 77, -4, 27, -17, 43, -77, 40, -21, 52, -7, 69, -39, 26, -45, 19, -97, 49, -7, 18, -125"
# arr = list(map(int,s.split(", ")))
# lis = [arr[0]]
# for i in range(1,len(arr)):
#     lis.append(lis[i-1]+arr[i])
# print(max(lis)+doctor)

# s = "40 -14 7 6 5 -4 -1 -1 40 7 6 5"
# arr = list(map(int,s.split()))
# print(sum(arr))

# nums = [-2,1,-1,3]
# cu = nums[0]
# maxa = nums[0]
# jo = nums[0]
# ko = nums[0]
# for i in range(1,len(nums)):
#         ko*=nums[i]
#         cu = max(cu*nums[i],nums[i])
#         jo = min(jo*nums[i],nums[i])
#         maxa = max(cu,maxa,jo*maxa,jo,ko)
# print(maxa)



t = int(input())
for i in range(t):
        n = int(input())
        matx = []
        # maty = []
        for j in range(n):
                x,y = map(int,input().split())
                matx.append([x,y])
                # maty.append([y,x])
        matx.sort()
        minx = matx[0][0]
        maxx = matx[-1][0]

        sxsy = -1
        sxby = -1
        bxsy = -1
        bxby = -1

        for i in range(n):
                if matx[i][0] == minx:
                        if sxsy == -1:
                                sxsy = matx[i]
                        sxby = matx[i]
                if matx[i][0] == maxx:
                        if bxsy == -1:
                                bxsy = matx[i]
                        bxby = matx[i]

        print(sxsy)
        print(sxby)
        print(bxsy)
        print(sxsy)

        


