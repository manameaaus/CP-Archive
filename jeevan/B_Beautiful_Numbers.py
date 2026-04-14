# t = int(input())
# for i in range(t):
#     kkk = input()
    
#     digits = [int(i) for i in kkk]

#     mina1 = float('inf')
#     mina2 = float('inf')

#     cur = digits[0]
#     digits = sorted(digits[1:])
#     for i in range(len(digits)):
#         cur += digits[i]
#         if cur > 9:
#             mina1 = len(digits)-i
#             break
#     else:
#         mina1 = 0


#     cur = 1
#     for i in range(len(digits)):
#         cur += digits[i]
#         if cur > 9:
#             mina2 = len(digits)-i+1
#             break
#     else:
#         mina2 = 1

#     print(min(mina1,mina2))




# test=int(input())
# for _ in range(test):
#     sumi=0
#     n=int(input())
#     h=str(n)
#     l=list(h)
#     dic={}
#     for i in l:
#         dic[int(i)]=dic.get(int(i),0)+1
#         sumi+=int(i)
#     h=9
#     count=0
#     while sumi>=10:
#         if dic.get(h,0)!=0:
#             if dic.get(h,0)==1 and  h==int(l[0]):
#                 count+=1
#                 sumi-=(h-1)
#                 dic[h]=0
#                 dic[1]=dic.get(1,0)+1
#                 h-=1
#             else:
#                 a=h*dic.get(h,0)
#                 tocheck = sumi - a
#                 if tocheck>=10:
#                     sumi-=a
#                     count+=dic.get(h,0)
#                     h-=1
#                 else:
#                     x=1
#                     while sumi-h*x>=10:
#                         x+=1
#                     sumi-=h*x
#                     count+=x
#         else:
#             h-=1
#     print(count)







test=int(input())
for _ in range(test):
    sumi=0
    n=int(input())
    h=str(n)
    l=list(h)
    dic={}
    for i in l:
        dic[int(i)]=dic.get(int(i),0)+1
        sumi+=int(i)
    h=9
    count=0
    while sumi>=10:
        if dic.get(h,0)!=0:
            if dic.get(h,0)==1 and  h==int(l[0]):
                count+=1
                sumi-=(h-1)
                dic[h]=0
                dic[1]=dic.get(1,0)+1
                h-=1
            else:
                a=h*dic.get(h,0)
                tocheck = sumi - a
                if tocheck>=10:
                    if h==int(l[0]):
                        sumi-=(a-1)
                        dic[1]=dic.get(1,0)+1
                    count+=dic.get(h,0)
                    h-=1
                else:
                    x=1
                    while sumi-h*x>=10:
                        x+=1
                    if x==dic.get(h,0) and h==int(l[0]):
                        sumi-=(h*x-1)
                        count+=x
                        h-=1
                    else:
                        sumi-=(h*x)
                        count+=x
                        break
                    
        else:
            h-=1
    print(count)






test=int(input())
for i in range(test):
    n=int(input())
    dic={}
    sumi = 0 
    first = 0
    while n>0:
        if n//10<=0:
            sumi+=(n%10)
            first = (n%10)
            break
        a=n%10
        sumi+=a
        dic[a]=dic.get(a,0)+1
        n=n//10
    is_found=False
    if dic:
        dic = dict(sorted(dic.items(), key=lambda x: x[0], reverse=True))
        sumi-=9
        count=0
        for i in dic:
            if i==0:
                continue
            if sumi<=0:
                break
            if i<first and not is_found:
                sumi-=(first-1)
                count+=1
                is_found=True
            else:
                n=sumi//i
                if dic[i]>=n+1:
                    count+=(n+1)
                    break
                else:
                    sumi-=dic[i]*i
                    count+=dic[i]
        print(count)
    else:
        print(0)