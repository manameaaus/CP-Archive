# t = int(input())
# for i in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))
#     # pot = []
#     ans = 0
#     def solve(a,pre,cl,idx):
#         global ans
#         if a==[]:
#             ans+=1
#             # pot.append(1)
#             return
#         if pre=="Liar":
#             if a[0]==cl:
#                 solve(a[1:],"Truth",cl)
            
#         if pre=="Truth":
#             if a[0]==cl:
#                 solve(a[1:],"Truth",cl)
#             solve(a[1:],"Liar",cl+1)

        
#     solve(a,"Truth",0)
#     print(ans%998244353)


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    # pot = []
    ans = 0
    def solve(pre,cl,idx):
        global ans
        if idx==n:
            ans+=1
            # pot.append(1)
            return
        if pre=="Liar":
            if a[idx]==cl:
                solve("Truth",cl,idx+1)
            
        if pre=="Truth":
            if a[idx]==cl:
                solve("Truth",cl,idx+1)
            solve("Liar",cl+1,idx+1)

        
    solve("Truth",0,0)
    print(ans%998244353)