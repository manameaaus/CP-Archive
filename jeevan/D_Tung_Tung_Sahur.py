# t = int(input())
# for i in range(t):
#     p = input()
#     s = input()

#     l = []
#     k = []

#     s1 = p[0]
#     s2 = s[0]

#     c = 0
#     curr = p[0]
#     for u in p:
#         if u != curr:
#             s1 += u
#             l.append(c)
#             c = 1
#             curr = u
#         else:
#             c += 1
#             pass
            
#     if curr == p[-1]:
#         l.append(c)


#     c = 0
#     curr = s[0]
#     for x in s:
#         if x != curr:
#             s2 += x
#             k.append(c)
#             c = 1
#             curr = x
#         else:
#             c += 1
#             pass
            
#     if s[-1] == curr:
#         k.append(c)

#     if len(l) == len(k) and s1 == s2:
#         ans = "YES"
#         for i in range(len(l)):
#             if k[i] >= l[i] and k[i] <= l[i] * 2:
#                 continue
#             else:
#                 ans = "NO"
#                 break
#         print(ans)
#     else:
#         print("NO")

        
t = int(input())
for i in range(t):
    p = input()
    s = input()
    letter1 = p[0]
    letter2 = s[0]
    l = []
    k = []

    c = 0
    curr = p[0]
    for i in p:
        if i == curr:
            c += 1
            pass
        else:
            # letter1 += i
            l.append(c)
            c = 1
            curr = i

    if curr == p[-1]:
        l.append(c)


    c = 0
    curr = s[0]
    for i in s:
        if i == curr:
            c += 1
            pass
        else:
            # letter2 += i
            k.append(c)
            c = 1
            curr = i

    if s[-1] == curr:
        k.append(c)

    if len(l) != len(k) or letter1 != letter2:
        print("NO")
    else:
        for i in range(len(l)):
            if  k[i] > l[i] * 2 or k[i] < l[i]:
                print("NO")
                break
        else:
            print("YES")






    # print(l)



# print(1)
# print("LR"*200000)
# print("LR"*200000)