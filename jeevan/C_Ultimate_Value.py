t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))

    if n == 1:
        print(l[0])
        break

    alice = []
    bob = []

    a = 0
    b = 0

    maxa = 0


    for i in range(n):
        if i%2==0:
            alice.append([l[i],(i+1)])
            a += l[i]
            maxa =  i
        else:
            bob.append([l[i],(i+1)])
            b += l[i]
            maxa111 = i


    alice.sort()
    bob.sort()

    # print(alice)
    # print(bob)

    c = alice[0][0]
    d = bob[-1][0]

    id1 = bob[-1][1]
    id2 = -alice[-1][1]

    k_bob = []
    p_alice = []

    for i in bob:
        if i[0] == d:
            k_bob.append(i[1])
            if d == c:
                p_alice.append(i[1])

    for i in alice:
        if i[0] == c:
            p_alice.append(i[1])
            if c == d:
                k_bob.append(i[1])
        

    k_bob.sort()
    p_alice.sort()


    extra = max(abs(p_alice[-1] - k_bob[0]),abs(p_alice[0] - k_bob[-1]))
    print(a-b + max(maxa,2*d-2*c+extra,max))