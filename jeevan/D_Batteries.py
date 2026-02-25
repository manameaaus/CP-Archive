def solve():
    n = int(input())
    for i in range(1,n):
        for j in range(1,n-i+1):
            print(j + i,j)
            k = int(input())
            if k:
                return
    return
t = int(input())
for i in range(t):
    solve()
    

# def solve():
#     n = int(input())
#     for i in range(1,n):
#         for j in range(1,n+1):
#             if i+j <= n:
#                 print(j,i+j)
#                 x = int(input())
#                 if x == 1:
#                     return
    
 
#     return
 
 
# testcase = 1
# testcase = int(input()) 
# for _ in range(testcase):
#     solve()

                