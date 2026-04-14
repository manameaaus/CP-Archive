import math
t = int(input())
for i in range(t):
    n = int(input())
    arr = [0] + list(map(int,input().split()))

    dp = [0] * (n+1)

    
    dp[1] = 0
    if arr[1] == arr[2]:
        dp[2] = 0
    else:
        dp[2] = 1

    two,one = max(arr[1],arr[2]),math.gcd(arr[1],arr[2])
    

    for i in range(3,n+1):
        # if i == 5:
        #     print(one,two,math.gcd(one,arr[i]))
        if math.gcd(one,arr[i]) < one:
            # print("je")
            

            two,one = one,math.gcd(one,arr[i]) 
            dp[i] = i-1
        else:
            if math.gcd(two,arr[i])>one:
                dp[i] = dp[i-1] + 1
                # print("pagal je"))
                # two,one =math.gcd(two,arr[i]),math.gcd(one,one,arr[i])
            else:
                dp[i] = dp[i-1]
                two,one = one,math.gcd(one,arr[i]) 

                # print("pagal pagal ppahgal je")
        # print(i,dp[:i+1])
    print(*dp[1:])


    

