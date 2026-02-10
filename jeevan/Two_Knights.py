# n = int(input())
# print(0)
# for i in range(2,n+1):
#     print((i**2-2)*(i**2-2)//2)

n = int(input())
print(0)
for i in range(2,n+1):
    x = i**2
    print((x*(x-1)//2)-(4*(i-1)*(i-2)))
