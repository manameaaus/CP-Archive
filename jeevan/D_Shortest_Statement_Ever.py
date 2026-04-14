# def msb(num):
#     bit = 0
#     while num:
#         bit += 1
#         num //= 2
#     return bit



    
# def solve1(p,q):
#     # return 1 << (msb(p)),q
#     mb = msb(p&q)
#     for bit in range(mb):
#         if (1 & (p >> bit)):
#             p -= 1 << bit
#     p |= (1 << (mb))
#     return p,q

# def solve2(p,q):
#     for bit in range(msb(p&q)):
#         if (1 & (p >> bit) == 0) and (1 & (q >> bit) == 0):
#             p |= 1 << bit
#         elif (1 & (p >> bit) == 1) and (1 & (q >> bit) == 1):
#             p -= 1 << bit
#     return p,q

    
# t = int(input())
# for i in range(t):
#     # x , y = map(lambda x: int(x, 2), input().split())
#     x , y = map(int,input().split())
#     # print(x,y)

#     dabba = []

#     dabba.append(solve1(x,y))
#     # dabba.append(solve2(x,y))

#     dabba.append(solve1(y,x)[::-1])
#     # dabba.append(solve2(y,x)[::-1])

#     dabba.append((x ^ (x&y),y))
#     dabba.append((x,y ^ (x & y)))

#     mina = 1 << 19
#     p,q = x,y

#     for p1,q1 in dabba:
#         if (p1 & q1 == 0) and (abs(p1-x) + abs(q1-y)) < mina:
#             p,q = p1,q1
#             mina = (abs(p1-x) + abs(q1-y))
#         # print(p1,q1)

#     print(p,q)
    


#     # p2,q2 = solve(y,x)

#     # if (abs(p1-x) + abs(q1-y)) < (abs(p2-x) + abs(q1-y))
#     # print(p1,q1)



#     # if (p1 & q1 == 0) and (abs(p1-x) + abs(q1-y)) < mina:
#     #     p,q = p1,q1
#     #     mina = (abs(p1-x) + abs(q1-y))
#     # if (p2 & q2 == 0) and (abs(p2-x) + abs(q2-y)) < mina:
#     #     p,q = p2,q2
#     #     mina = (abs(p2-x) + abs(q2-y))
#     # if (p3 & q3 == 0) and (abs(p3-x) + abs(q3-y)) < mina:
#     #     p,q = p3,q3
#     #     mina = (abs(p3-x) + abs(q3-y))
#     # if (p4 & q4 == 0) and (abs(p4-x) + abs(q4-y)) < mina:
#     #     p,q = p4,q4
#     #     mina = (abs(p4-x) + abs(q4-y))
    


#     # # q1,p1 = solve1(y,x)
#     # p1,q1 = solve2(x,y)
    
#     # print(format(p,'011b'))
#     # print(format(q,'011b'))

#     # p2,q2 = solve1(x,y)
#     # print(format(p2,'011b'))
#     # print(format(q2,'011b'))

#     # print(p2,q2)

#     # print(p1,q1)
#     # # print(format(p2,'018b'))
#     # print(format(x,'020b'))
#     # # print(format(q2,'018b'))
#     # print(format(y,'020b'))





# # print(1 & (6 >> 1) == 1)




def msb(num):
    bit = 0
    while num:
        num >>= 1
        bit += 1
    return bit

def solve1(p,q):
    mb = msb(p&q)
    for bit in range(31):
        if bit < mb:
            if ((p >> bit) & 1):
                p ^= 1 << bit
        else:
            if ((p >> bit) & 1):
                p ^= 1 << bit
            else:
                p |= 1 << bit
                break
    return p,q

def solve2(p,q):
    mb = msb(p&q)
    p ^= (p&q)
    for bit in range(mb):
        if (((p >> bit) & 1 == 0) and ((q >> bit) & 1 == 0)):
            p |= 1 << bit
    
    return p,q

t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    
    dabba = []

    dabba.append(solve1(x,y))
    dabba.append(solve2(x,y))

    dabba.append(solve1(y,x)[::-1])
    dabba.append(solve2(y,x)[::-1])

    p,q = x,y
    mina = 1 << 32

    for p1,q1 in dabba:
        if ((p1 & q1 == 0) and (abs(p1-x) + abs(q1-y) < mina)):
            mina = abs(p1-x) + abs(q1-y)
            p,q = p1,q1

    print(p,q)


# print(format(x,'031b'))
    # print(format(y,'031b'))
    # print()


     # print(format(p1,'031b'))
        # print(format(q1,'031b'))
        # print()