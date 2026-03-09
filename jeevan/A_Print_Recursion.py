def recur(n):
    if n == 0:
        return
    print("I love Recursion")
    recur(n-1)
n = int(input())
recur(n)
