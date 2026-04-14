# t = int(input())
# for i in range(t):
#     n = int(input())
#     l = list(map(int,input().split()))
#     d = {}
#     ans = 0
#     for i in l:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     xx = len(d)
#     s2 = sum(1 for i in d if d[i]==2)

#     if xx%2==0:
#         ans+=xx//2

#         if s2%2:
#             ans+=s2//2+1
#         else:
#             ans+=s2//2

#     else:
#         ans+=xx//2+1
#         ans+=s2//2

    
#     s1 = sum(1 for i in d if d[i]==1)
#     if s1%2:
#         ans+=s1//2+1
#     else:
#         ans+=s1//2

        
    
#     print(ans)


t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    ans = 0
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    xx = len(d)
    s1 = sum(1 for i in d if d[i]==1)
    rem = xx-(s1)
    if (s1%2==0): 
        ans+=s1
    elif (s1%2==1):
        ans+=(s1//2+1)*2
    ans+=rem
    print(ans)


