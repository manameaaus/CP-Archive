t = int(input())
ref = [1,3,6,10,15]
limit = [2,1,4,2,15]

def check(n,idx):
    if n < 0:
        return float('inf')
    
    if idx == 4:
        return float('inf') if n%15 else n//15
    
    cost = float('inf')
    for lll in range(limit[idx]+1):
        cost = min(cost,check(n - (lll * ref[idx]),idx+1) + lll)
    return cost

for i in range(t):
    n = int(input())
    print(check(n,0))

# [1,3,6,10,15]
# [3,2,4,2,15]
# 6 12 18 24 30 