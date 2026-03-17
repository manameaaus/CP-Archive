def main():
    n,m = map(int,input().split())
    freq = [0] * (m+1)
    dabba = []


    for i in range(n):
        l = list(map(int,input().split()))
        for i in range(1,l[0]+1):
            freq[l[i]] += 1
        dabba.append(l)

    for i in range(1,m): 
        if not freq[i]:
            print("NO")
            return
        
    c = 0
    for lis in dabba:
        pos = True
        for i in range(1,lis[0]+1):
            freq[l[i]] += 1


t = int(input())
for i in range(t):
    main()


