# n,m = map(int,input().split())
# a = list(map(int,input().split()))
# x = n
# a.sort()
# maxa = 0
# mina = 0

# for i in range(m):
#     if a[i] <= n:
#         mina += int(a[i]*(a[i]+1)/2)
#         n -= a[i]
#     else:
#         mina += int((a[i] * (a[i] + 1)) / 2) - int((a[i]-n) * (a[i]-n + 1) / 2)
#         break

# a.reverse()
# n = x
# for i in range(m):
#     if i<m-1 and n >= a[i] - a[i+1] + 1:
#         maxa += int((a[i] * (a[i] + 1)) / 2) - int(((a[i+1]-1) * ((a[i+1]-1) + 1)) / 2)
#         n -= a[i] - a[i+1] + 1
#     else:
#         maxa += int((a[i] * (a[i] + 1)) / 2) - int((a[i]-n) * (a[i]-n + 1) / 2)
#         break
   
    

    

# print(maxa,mina)



# import heapq

# def min_max_earnings(n, m, planes):
#     min_heap = planes[:]
#     heapq.heapify(min_heap)
#     max_heap = [-p for p in planes]
#     heapq.heapify(max_heap)
    
#     min_earning, max_earning = 0, 0
    
#     for _ in range(n):
#         min_price = heapq.heappop(min_heap)  # Get the cheapest available ticket
#         min_earning += min_price
#         if min_price > 1:
#             heapq.heappush(min_heap, min_price - 1)  # Reduce seat count and push back
#     for _ in range(n):
#         max_price = -heapq.heappop(max_heap)  # Get the most expensive available ticket
#         max_earning += max_price
#         if max_price > 1:
#             heapq.heappush(max_heap, -(max_price - 1))  # Reduce seat count and push back
#         print(max_heap)

#     print(max_earning, min_earning)



import heapq

def min_max_earnings(n, m, planes):
    min_heap = planes[:]
    max_heap = [-p for p in planes]
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    min_ans = 0
    max_ans = 0

    for i in range(n):
        min_price = heapq.heappop(min_heap)
        min_ans += min_price
        if min_price > 1:
            heapq.heappush(min_heap , min_price -1)

    for i in range(n):
        max_price = -heapq.heappop(max_heap)
        max_ans += max_price
        if max_price > 1:
            heapq.heappush(max_heap , -(max_price - 1))
    print(max_ans,min_ans)


n, m = map(int, input().split())
planes = list(map(int, input().split()))
min_max_earnings(n, m, planes)

