t = int(input())
for i in range(t):
    k = int(input())

    t = []
    for i in range(1000000):
        temp = []
        while i:
            temp.append(i%10)
            i//=10

        t.extend(temp[::-1])

    print((t))

    

