# t = int(input())
# for i in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

#     ans = 0
#     # i = 0
#     # j = n-1
#     # while i < n and j >= 0:
#     #     if a[i] % 2 == 0:
#     #         a[i],a[j] = a[j],a[i]
#     #         j -= 1
#     #     else:
#     #         i += 1

#     # for i in range(n):
#     #     if a[i] % 2 == 1:




#     # i = 0
#     # j = n-1
#     # while i < n and j >= 0:
#     #     if b[i] % 2 == 1:
#     #         b[i],b[j] = b[j],b[i]
#     #         j -= 1
#     #     else:
#     #         i += 1
#     odd  = []
#     even = []
#     for i in range(n):
#         if a[i] % 2 == 0 and b[i] % 2 == 1:
#             print(3,i)
#         if a[i] % 2 == 1 and b[i] % 2 == 1:
#             odd.append(i)
#         if a[i] % 2 == 0 and b[i] % 2 == 0:
#             even.append(i)


#     for k in range(len(odd)):
#         print(1,odd[])



#     print(a)
    

        

T = int(input())
for _ in range(T):
    size = int(input())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    actions = []
 
    for idx in range(size):
        if first[idx] > second[idx]:
            first[idx], second[idx] = second[idx], first[idx]
            actions.append([3, idx + 1])
    for i in range(size):
        for j in range(size - 1 - i):
            if second[j] > second[j + 1]:
                second[j], second[j + 1] = second[j + 1], second[j]
                actions.append([2, j + 1])
    for i in range(size):
        for j in range(size - 1 - i):
            if first[j] > first[j + 1]:
                first[j], first[j + 1] = first[j + 1], first[j]
                actions.append([1, j + 1])
    print(len(actions))
    for act in actions:
        print(*act)