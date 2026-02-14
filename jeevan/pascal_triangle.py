def pascal_triangle(n):
    if n==1:
        return [1]
    xx = pascal_triangle(n-1)
    l = [1]
    for i in range(n-2):
        l.append(xx[i]+xx[i+1])
    l.append(1)
    print(*l)
    return l
n = int(input())
pascal_triangle(n)


