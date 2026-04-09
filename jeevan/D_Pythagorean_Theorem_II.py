# def hot(a,b,n):
#     global c
#     x = (a**2+b**2)**(0.5)
#     if x>n:
#         return 0
#     if x==int(x) and a<b:
#         print(a,b,x)
#         c+=1
#     hot(a,b+1,n)
#     hot(a+1,b+1,n)
#     # if a<b:
#     #     hot(a+1,b,n)

n = int(input())
c = 0
a = 1
b = 1
univ = n**2
while a**2<univ/2:
    dog = a**2
    while dog+(b**2)<=univ:
        x = (dog+b**2)**(0.5)
        if x==int(x):
            c+=1
        b+=1
    a+=1
    b=a

print(c)
# for i in cop:
#     print(i)


# 2n, n^2-1, n^2 + 1
# c = 0
# x = 2
# while (x**2+1)**2<=n**2:
#     vovovov = x**2
#     joker = (vovovov+1)**2
#     ko    = 4*vovovov
#     po    = (vovovov-1)**2
#     if ko+po==joker:
#         print(vovovov,vovovov-1,vovovov+1)
#         c+=1
#     x+=1

# print(c)
