# t = int(input())
# for i in range(t):
#     n , m = map(int,input().split())
#     a = list(map(int,input().split()))
#     b = int(input())
#     if n>1:
#         if (b-a[0] <= a[1] or a[0] <= a[1]) and ((b-a[-1] >= a[-2] or a[-1] >= a[-2]) or (b-a[-1] >= b-a[-2] or a[-1] >= b-a[-2])):
            
#             for i in range(1,n-1):
#                 if (a[i-1] <= a[i] and a[i] >= a[i+1]) or (a[i-1] <= b-a[i] and a[i] >= b-a[i+1]) or (b-a[i-1] <= a[i] and a[i] >= a[i+1]) or (a[i-1] <= a[i] and a[i] >= b-a[i+1]) or (b-a[i-1] <= b-a[i] and b-a[i] >= a[i+1]) or (a[i-1] <= b-a[i] and b-a[i] >= b-a[i+1]) or (b-a[i-1] <= b-a[i] and b-a[i] >= b-a[i+1]) or (b-a[i-1] <= a[i] and a[i] >= b-a[i+1]):
#                     continue
#                 else:
#                     print("NO")
#                     break
#             else:
#                 print("YES")
#         else:
#             print("NO")
#     else:
#         print("YES")
#to do more

j = 0
def solve(a,b,i,c,j):
    j += 1
    # j += 1
    # if i == 4:
    #     print(c == sorted(c))
    if i==n:
        return (c == sorted(c))
        # if c == sorted(c):
        #     # print(c)
        #     return True
        # return False
    c.append(a[i])
    x = solve(a,b,i+1,c,j)
    if x:
        print(i,c,j)
        return x
    else:
        j += 1
        c = c[:i-1]
        c.append(b-a[i])
        # c[-1] = b-a[i]
        # print("o",i,c)

        return solve(a,b,i+1,c,j)

        

t = int(input())
for i in range(t):
    n , m = map(int,input().split())
    a = list(map(int,input().split()))
    b = int(input())
    if solve(a,b,0,[],0):
        print("YES")
    else:
        print("NO")





