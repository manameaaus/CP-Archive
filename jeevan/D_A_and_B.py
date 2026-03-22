t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    ans1 = 0
    ans2 = 0

    indb = [i for i in range(n) if s[i] == 'b']
    inda = [i for i in range(n) if s[i] == 'a']


    if not inda or not indb:
        print(0)
    else:
        stb = len(indb)//2
        st = len(indb)//2
        c = 0
        while st >= 0:
            ans1 += indb[stb]-indb[st]-c
            c += 1
            st-=1

        st = len(indb)//2
        c = 0
        while st < len(indb):
            ans1 += indb[st]-indb[stb]-c
            c += 1
            st+=1



        sta = len(inda)//2
        st = len(inda)//2
        c = 0
        while st >= 0:
            ans2 += inda[sta]-inda[st]-c
            c += 1
            st-=1

        st = len(inda)//2
        c = 0
        while st < len(inda):
            ans2 += inda[st]-inda[sta]-c
            c += 1
            st+=1

        print(min(ans1,ans2))
