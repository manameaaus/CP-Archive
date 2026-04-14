# t = int(input())
# for i in range(t):
#     # print(i,"hello")
#     n = int(input())
#     a = list(map(int,input().split()))
#     d = {}
#     for i in a:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     f2 = []
#     f3 = []
#     f4 = []
#     f1 = []
#     for i in d:
#         if d[i]==2:
#             f2.append(i)
#         elif d[i]==3:
#             f3.append(i)
#         elif d[i]==1:
#             f1.append(i)
#         else:
#             f4.append(i)
#     # print(f2)       
#     a.sort()
#     f1.sort()
#     f3.sort()
#     f2.sort()
#     if len(f4)>0:
#         print(f4[0],f4[0],f4[0],f4[0])
#     elif len(f3)>0:
#         for i in range(n-1,-1,-1):
#             if a[i]<3*f3[0] and a[i]!=f3[0]:
#                 print(f3[0],f3[0],f3[0],a[i])
#                 break
#         else:
#             if len(f2)==1:
#                 if f1[-1]<2*f2[-1]+f1[-2]:
#                     print(f2[-1],f2[-1],f1[0],f1[1])
#                 else:
#                     print(-1)
#             elif len(f2)>1:
                
#                 print(f2[0],f2[0],f2[1],f2[1])
#             else:
#                 print(-1)
#     elif len(f2)==1:
#             # print(f1)
#             for i in range(len(f1)-1,0,-1):
#                 if f1[i]<2*f2[-1]+f1[i-1]:
#                     print(f2[-1],f2[-1],f1[i],f1[i-1])
#                     break
#             else:
#                 print(-1)
#     elif len(f2)>1:
#         print(f2[0],f2[0],f2[1],f2[1])
#     else:
#         print(-1)
    

    
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    frequency = {}
    for num in a:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] == 4:
            print(num, num, num, num)   
            break
        # else:
        #     if frequency[num] == 3:


    f1, f2, f3, f4 = [], [], [], []
    for num, count in frequency.items():
        if count > 3:
            f4.append(num)
        elif count == 3:
            f3.append(num)
        elif count == 2:
            f2.append(num)
        else:
            f1.append(num)

    a.sort()
    f1.sort()
    f2.sort()
    f3.sort()

    result = []

    if f4:
        result = [f4[0], f4[0], f4[0], f4[0]]
    elif f3:
        for num in reversed(a):
            if num < 3 * f3[0] and num != f3[0]:
                result = [f3[0], f3[0], f3[0], num]
                break
        else:
            if len(f2) == 1 and len(f1) > 1:
                if f1[-1] < 2 * f2[0] + f1[-2]:
                    result = [f2[0], f2[0], f1[-1], f1[-2]]
                else:
                    result = [-1]
            elif len(f2) > 1:
                result = [f2[0], f2[0], f2[1], f2[1]]
            else:
                result = [-1]
    elif len(f2) >= 2:
        result = [f2[0], f2[0], f2[1], f2[1]]
    elif len(f2) == 1 and len(f1) > 1:
        for i in range(len(f1) - 1, 0, -1):
            if f1[i] < 2 * f2[0] + f1[i - 1]:
                result = [f2[0], f2[0], f1[i], f1[i - 1]]
                break
        else:
            result = [-1]
    else:
        result = [-1]

    print(*result)