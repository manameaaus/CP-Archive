def prr(k):
    if k == 0:
        return
    print(' ' * (n-k),'*' * (2*k-1),sep = "")
    prr(k-1)

n = int(input())
prr(n)