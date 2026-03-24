def recur(num,d,steps):
    # print(num,d,steps)
    if num == 1:
        print(steps)
        return
    if steps > 120:
        return
    
    if num%2 == 0:
        recur(num//2,d,steps+1)
    elif num > d:
        recur(num-d,d,steps+1)
    

t = int(input())
for i in range(t):
    n,d = map(int,input().split())
    recur(n,d,0)
    # l = []
    # st = 1
    # while st <= n:
    #     l.append(st)
    #     st *= 2


    
    # mina = float('inf')
    # for i in range(len(l)):
    #     for j in range(min(n//d + 1,61)):
    #         if l[i] + (d * j) == n:
    #             mina = min(mina,i+j)
    #             if(i+j == 7 ):
    #                 print(l[i],j)
    # print(mina)



            
    