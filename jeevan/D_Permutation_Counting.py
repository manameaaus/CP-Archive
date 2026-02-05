def check(mid,k):
    currr = sum(max(0,mid-i) for i in freq)
    # for i in freq:
    #     if i < mid:
    #         currr += mid - i

    return currr <= k

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    freq = list(map(int,input().split()))

    st = 0
    en = (sum(freq)+k) // n
    ans = 0

    while st <= en:
        mid = (st + en) // 2
        if check(mid,k):
            ans = mid
            st = mid + 1
        else:
            en = mid - 1

    non_zero = 0
    pot = k
    for i in range(n):
        if freq[i] < ans:
            pot -= ans - freq[i]
        elif freq[i] > ans:
           non_zero += 1

    print((ans * n) - (n-1)  + non_zero + pot)

# 1 2 3 4 
# 6 6 7 4 6
# 6 6 7 6 6

# 3 1 2 4 5 | 3 1 2 4 5 | 3 1 2 4 5 | 3 1 2 4 5 | 3 1 2 4 5 | 3 1 2 4 5 | 3 1