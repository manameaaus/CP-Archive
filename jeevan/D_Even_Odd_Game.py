t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))


    even = [i for i in arr if i % 2 == 0]
    odd = [i for i in arr if i % 2]

    if len(even) == 0 and n > 1:
        print('Bob')
    elif len(even) == 0 and n == 1:
        print('Tie')


    

    
    

    

    

