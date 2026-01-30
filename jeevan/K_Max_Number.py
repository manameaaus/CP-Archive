def maxa(idx):
    if idx == n:
        return -float("inf")
    return max(a[idx],maxa(idx+1))

n = int(input())
a = list(map(int,input().split()))
print(maxa(0))