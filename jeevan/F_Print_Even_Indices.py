def prr(i):
    if i == n:
        return
    prr(i+1)
    if i % 2 == 0:
        print(arr[i],end = " ")

n = int(input())
arr = list(map(int,input().split()))
prr(0)