t= int(input())
for i in range(t):
    n = int(input())
    print((n//15)*3 + min(3,n-((n//15)*15)+1))