def calc(num):
    c = 0
    while num%10 == 0:
        c += 1
        num//=10

    return c
t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    d = [calc(i) for i in l]
    d.sort(reverse = True)
    whole_length = sum(len(str(i)) for i in l)

    for i in range(0,len(d),2):
        if not d[i]:
            break
        whole_length -= d[i]

    if whole_length > m:
        print("Sasha")
    else:
        print("Anna")

    # print(d)

    

