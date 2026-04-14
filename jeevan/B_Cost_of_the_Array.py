# t =  int(input())
# for i in range(t):
#     n,k = map(int,input().split())
#     a = list(map(int,input().split()))
#     look = 1
#     kaddi = 0
#     for i in range(1,n):
#         print(n-i-1,k-kaddi-1,i)
#         if n-i<k-kaddi-1:
#             look+=1
#             kaddi+=1
#         if a[i] != look:
#             print(look)
#             break
#     else:
#         print(look) 
        
        

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if n == k:
        c = -1
        for i in range(1, n, 2):  
            if arr[i] != (i // 2) + 1:
                c = (i // 2) + 1
                break
        if c == -1:
            c = (n // 2) + 1
        print(c)
    else:
        l = -1
        for i in range(1, n - k + 2):
            if arr[i] != 1:
                l = i + 1 
                break
        
        if l == -1:
            m = 2
            for i in range(n - k, n, 2):
                if arr[i] != m:
                    break
                m += 1
            print(m)
        else:
            print(1)