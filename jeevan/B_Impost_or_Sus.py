# border - ceil
# odd - Floor
# sususus


t = int(input())
for i in range(t):
    s = list(input())

    ans = 0
    curr = s[0]
    c = 0
    check = 0

    if curr == 's':
        check += 1

    dabba = []

    for i in s:
        
        if i == curr:
            c += 1
        else:
            # print(i)
            if i == 's': 
                dabba.append(c)
                check += 1
            c = 1
            curr = i

    if s[-1] == "u":
        dabba.append(c)

    # print(check,dabba)

    if s.count('u') == 0:
        print(0)
    else:
        if s.count('s') == 1 or check == 1:
            for i in dabba:
                ans += (i + 1) // 2

        elif s.count('s') >= 2:
            for i in range(1,len(dabba)-1):
                ans += dabba[i]//2

            
            if len(dabba) > 1:
                if s[0] == "s":
                    ans += dabba[0]//2
                else:
                    ans += (dabba[0] + 1) // 2

                if s[-1] == 's':
                    ans += dabba[-1]//2
                else:
                    ans += (dabba[-1] + 1) // 2
            else:
                ans += dabba[0]//2
                
            
        else:
            ans = len(s) // 2 + 1

        print(ans)
        


