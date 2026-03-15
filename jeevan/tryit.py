# r,c = map(int,input().split())
# miss = [0]*5

# mat = [[i for i in input()] for i in range(r)]
# # print(mat[0][1])
# for i in range(r-1):
#     for j in range(c-1):
#         l = [mat[i][j],mat[i][j+1],mat[i+1][j],mat[i+1][j+1]]
#         if l.count("#") == 0:
            
#             miss[l.count("X")] += 1
            
# for i in range(0,5):
#     print(miss[i])


# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
#     m = int(input())
# for i in range(m):
#     x = int(input())
#     ans = 10000000
#     pot = 0
#     for i in range(n):
#         for j in range(i+1,n):
#             if abs(x-l[i]-l[j]) < ans:
#                 pot = l[i]+l[j]
#                 ans = min(ans,abs(x-l[i]-l[j]))
#                 # print(l[i],l[j],ans)
            
#     print(f"Closest sum to {x} is {pot}.")


# for i in arr:
#     print(*i)



# t = int(input())
# arr = list(map(int, input().split()))
# n = max(arr)

# spf = list(range(n + 1))  

# for i in range(2, int(n**0.5) + 1):
#     if spf[i] == i:
#         for j in range(i * i, n + 1, i):
#             if spf[j] == j:
#                 spf[j] = i

# for i in range(t):
#     num = arr[i]
#     result = []
#     while num > 1:
#         result.append(spf[num])
#         num //= spf[num]
#     arr[i] = result

# for i in arr:
#     print(*i)

# print(1)
# print(100000,100000)
# for i in range(1,100001):
#     print(i,end=" ")
# print()
# for i in range(1,100000):
#     print(1,i,100000+i)
# print(2)


# import math

# MOD = int(1e9 + 7)

# def get_divisors(n):
#     divisors = set()
#     for i in range(1, int(math.isqrt(n)) + 1):
#         if n % i == 0:
#             divisors.add(i)
#             divisors.add(n // i)
#     return divisors

# def product_of_divisors(n):
#     divisors = get_divisors(n)
#     result = 1
#     for d in divisors:
#         result = (result * d) % MOD
#     return result

# # Example usage
# n = 44100
# print("Product of divisors of", n, "modulo 1e9+7 is:", product_of_divisors(n))


# import sys
# sys.stdin = open('foreign.in', 'r')
# sys.stdout = open('foreign.out', 'w')

# s = input()
# n = len(s)
# p = [0]*n
# p[0]=1
# cur = (1/n)
# for i in range(1, n):
#   p[i]=cur
#   if (i<n-1):
#     cur+=(p[i]*(1/(n-i)))



# w, c, rc, rw = 0, 0, 0, 0
# ans = [0]*n
# ans[0]=0
# if s[0]=='W':
#   w=p[0]
#   rw=p[0]*(1/n)
# else:
#   c=p[0]
#   rc=p[0]*(1/n)
# for i in range(1, n):
#   w-=rw
#   c-=rc
#   if s[i]=='W':
#     w+=p[i]
#     rw+=p[i]*(1/(n-i))
#     ans[i]=c
#   else:
#     c+=p[i]
#     rc+=p[i]*(1/(n-i))
#     ans[i]=w

# print(sum(ans))







# st = 4
# c = 4

# while c <= 4 * (1e6):
#     print(st,c)
#     st *= 2
#     c += c + st




# import random

# n = 2 * 100000  # number of nodes
# edges = []

# # We'll generate a random tree by connecting node i+1 to some previous node
# for i in range(2, n + 1):
#     # randomly connect to a node in [1, i-1] to ensure connectivity
#     parent = random.randint(1, i - 1)
#     edges.append((parent, i))

# # Output in edge format
# print(n)
# for u, v in edges:
#     print(u, v)
print("priyanshu")