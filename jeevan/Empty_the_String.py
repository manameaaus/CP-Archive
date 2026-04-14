t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    c = 0
    while s!="":
        j = ""
        if s[0]=="A":
            met1 = "B"
        else:
            met1 = "A"
        for i in s:
            if i==met1:
                j+=i
            else:
                met1=i
        s = j
        c+=1
        bc = s.count("B")
        sc = len(s)
        if bc==sc:
            c+=sc
            break
        elif bc==0:
            c+=sc
            break

    print(c)
                

       