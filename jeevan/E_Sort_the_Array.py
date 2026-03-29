# n = int(input())
# a = list(map(int,input().split()))
# jo = a[0]
# c = 0
# hot = []
# last = n+1
# for i in range(1,n):
#     if a[i]>=a[i-1]:
#         continue
#     else:
#         # if c==1:
#         #     print("no")
#         #     break

#         c += 1
#         if c==2:
#             print("no")
#             break
#         hot.append(i)
# else:
    
#     print("yes")
#     print(hot[0]+1,hot[-1]+1)


n = int(input())
a = list(map(int,input().split()))
c = 0
last = 0
first = 0

for i in range(1,n):
    if a[i]<=a[i-1] and c==1:
        last = i
    if a[i]>=a[i-1]:
        continue
    # elif a[i]>=a[i-1] and c==1:
    #     last = i
    else:
        if c==1:
            print("no")
            break
        c += 1
        first = i
        last  = i
else:
    print("yes")
    print(first+1,last+1)  # 1 2 3 4


