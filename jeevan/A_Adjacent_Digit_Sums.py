t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if (x+1 == y) or (y+8 == x) or ((x - y+ 1)%9 == 0 and (x>y)):
        print("Yes")
    else:
        print("No")

# t = int(input())
# for i in range(t):
#     x,y = map(int,input().split())
#     if y == x+1:
#         print("Yes")
#     elif y == x-8:
#         print("Yes")
#     elif y==1 and x%9 == 0:
#         print("Yes")
#     elif (x - y + 1)%9 == 0 and (x - y + 1)>0:
#         print("Yes")
#     else:
#         print("No")
    
    # elif 
    # 69 7 25 8