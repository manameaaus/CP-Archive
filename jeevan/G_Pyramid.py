
n = int(input())

def pattern(i):
    if i == n:
        return
    print(' ' * (n-i-1),'*' * (2*i+1),sep = '')
    pattern(i+1)


pattern(0)


