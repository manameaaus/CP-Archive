def calc(n):
    return (n * (n+1)) // 2
n = int(input())
print(2 * (calc(2*n) - calc(n)) + 2*n + 1)