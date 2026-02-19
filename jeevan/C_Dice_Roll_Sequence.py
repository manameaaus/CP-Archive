# t = int(input())
# for i in range(t):
#     n = int(input())
#     l = list(map(int,input().split()))
#     res = 0
#     i = 1
#     while i < n:
#         if (l[i] == l[i-1]) or (l[i] + l[i-1] == 7):
#             res += 1
#             i += 2
#         else:
#             i += 1

#     print(res)



                                    
test=int(input())
for i in range(test):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    if len(l)==2 and (l[0]+l[1]==7 or l[0]==l[1]):
        print(1)
    elif len(l)==2:
        print(0)
    else:
        for i in range(1,len(l)-1):
            if l[i]+l[i-1]==7 or l[i]==l[i-1] or l[i]==l[i+1]:
                count+=1
                c=6
                while c==l[i-1] or c==l[i+1] or c+l[i-1]==7 or c+l[i+1]==7:
                    c-=1
                l[i]=c
        print(count)
        print(l)
