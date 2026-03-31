t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input()]
    b = [int(i) for i in input()]
    
    score = 0
    temp = 0
    for i in range(n):
        if a[i]==1 and b[i]==1:
            score+=1
        elif (a[i]==1 and b[i]==0) or (a[i]==0 and b[i]==1):
            temp+=1

    if (score%2==0 and temp>0) or score%2:
        print("YES")
    else:
        print("NO")


    # ans = "NO"
    # for i in range(n):
    #     if (a[i]=="1" and b[i]=="0") or (a[i]=="1" and b[i]=="0"):
    #         ans = "YES"
    #         break
    # print(ans)