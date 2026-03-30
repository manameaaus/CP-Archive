# t = int(input())
# for i in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     if a.count(0) == 0:
#         print(1)
#         print(1,n)
#     elif a[0] == 0 and a[-1] == 0:
#         print(3)
#         print(1,2)
#         print(2,n-1)
#         print(1,2)
#     elif a[0] != 0:
#         print(2)
#         print(2,n)
#         print(1,2)
#     elif a[-1] != 0:
#         print(2)
#         print(1,n-1)
#         print(1,2)


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a.count(0) == 0:
        print(1)
        print(1,n)
    elif a[0] != 0:
        print(2)
        print(2,n)
        print(1,2)
    elif a[-1] != 0:
        print(2)
        print(1,n-1)
        print(1,2)
    else:
        print(3)
        print(3,n)
        print(1,2)
        print(1,2)
    