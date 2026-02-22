n = int(input())
l = []
for i in range(n):
 l.append(int(input()))
m = int(input())
for i in range(m):
    x = int(input())
    ans = 10000000
    pot = 0
    for i in range(n):
        for j in range(i+1,n):
            if abs(x-l[i]-l[j]) < ans:
               pot = l[i]+l[j]
            ans = min(ans,abs(x-l[i]-l[j]))
            # print(l[i],l[j],ans)
            
    print(f"Closest sum to {x} is {pot}.")