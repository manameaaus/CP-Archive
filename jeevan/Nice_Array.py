# t = int(input())
# for i in range(t):
#     n,k = map(int,input().split())
#     a = list(map(int,input().split()))
#     d = []
#     dgod = []
#     dgoast = []
#     dg = []
#     for i in a:
#         v = i/k
#         if v==int(v):
#             d.insert(-1,int(v))
#             dgod.append(int(v))
#         else:
#             dg.append(i)
#             dgoast.append(v)
#             d.insert(0,v)
#     print(dgod)
#     print(dgoast)
#     print(dg,k)
#     print(d)
#     if sum(d)==0:
#         print("YES")
#     elif dgoast==[]:
#         print("NO")

# t = int(input())
# for i in range(t):
#     n,k = map(int,input().split())
#     a = list(map(int,input().split()))
#     dgood = []
#     dbad = []
#     ddiff = []
#     dfinal = []
#     for i in a:
#         if i%k==0:
#             dfinal.append(i/k)
#             dgood.append(i/k)
#         else:
#             ddiff.append(i%k)
#             dbad.append(i//k)
#             dfinal.append(i//k)

#     # print(dgood,sum(dgood))
#     # print(dbad,sum(dbad))
#     # print(dfinal,sum(dfinal))
#     # print(ddiff,k)

#     hot = sum(dfinal)
#     if hot>0:
#         print("NO")
#     elif abs(hot)<=len(ddiff):
#         print("YES")

#     # elif sum(dgood)==0 and 


t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ddiff = []
    dfinal = []
    cp = 0
    cn = 0
    for i in a:
        dfinal.append(i//k)
        if i%k!=0:
            if i>=0:
                cp+=1
            else:
                cn+=1
    hot = sum(dfinal)
    if hot>0:
        print("NO")
    elif hot<=0:
        if cp>=hot:
            print("YES")
        else:
            print("NO")
    elif hot>0:
        if cn>=hot:
            print("YES")
        else:
            print("NO")

    
    

    
