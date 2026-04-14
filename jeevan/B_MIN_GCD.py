import math
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    god = a[0]
    if a.count(god)>1:
        print("yes")
    else:
        l = []
        for j in range(1,n):
            if a[j] % god == 0:
                l.append(a[j]//god)
        if len(l) == 0:
            print('no')
        else:
            ans = l[0]
            for i in range(1,len(l)):
                ans = math.gcd(ans,l[i])
            if ans == 1:
                print("yes")
            else:
                print('no')

        # odd = [i for i in l if i %2]
        # # print(l)
        # if len(l) < 2:
        #     print("no")
        # else:
        #     if len(odd) > 0 and len(odd) < len(l):
        #         print("yes")
        #     elif len(odd) == 0:
        #         print("no")
        #     else:
        #         for i in range(1,len(odd)):
        #             if math.gcd(odd[i],odd[i-1]) == 1:
        #                 print("Yes")
        #                 break
        #         else:
        #             if len(odd) > 1:
        #                 if math.gcd(odd[-1],odd[0]) == 1:
        #                     print("yes")
        #                 else:
        #                     print("no")


# print(998244359987710471%99824435698771045)
            


