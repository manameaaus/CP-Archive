t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    pre = [0]
    count = 0
    for i in range(n):
        pre.append(pre[-1]+arr[i])
    for i in range(1,int(max(pre)**(1/2))+1,2):
        if i**2 in pre:
            count+=1
    print(count)
    # print(pre)


        
    