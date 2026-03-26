def main():
        # n = int(input())
        # cur = 0

        # s = list(input())

        # dot = n
        # s_idx = n

        # last_dot = -1
        # p_idx = -1


        # pfx_s = [0 for i in range(n)]
        # pfx_p = [0 for i in range(n)]

        # for i in range(n):
        #     if s[i] == "s":
        #         cur += 1
        #         s_idx = min(s_idx,i)
        #     if s[i] == "p":
        #         if (cur >= 1):
        #             if dot < s_idx:
        #                 print("NO")
        #                 return
                    
        #     if s[i] == '.':
        #         dot = min(dot,i)

        # cur = 0
        # for i in range(n-1,-1,-1):
        #     if s[i] == "p":
        #         cur += 1
        #         p_idx = max(p_idx,i)
        #     if s[i] == "s":
        #         if (cur >= 1):
        #             if last_dot > p_idx:
        #                 print("NO..")
        #                 return
                    
        #     if s[i] == '.':
        #         last_dot = max(last_dot,i)
        
        # jee = n #p
        # nee = -1 #s
        # chatur = 0 #dot

        # for i in range(n):
        #     if s[i] == "p":
        #         jee = i
        #     elif s[i] == "s":
        #         nee = i
                  
        #     elif s[i] == '.':
        #         chatur = i

        
        # if (jee < nee):
        #     print("NO")
        #     return


            

        
        # print("YES")

        n = int(input())
        s = list(input())

        min_s = n
        min_p = n
        max_s = -1
        max_p = -1

        for i in range(n):
            if s[i] == "s":
                min_s = min(min_s,i)
                max_s = max(max_s,i)
            if s[i] == "p":
                min_p = min(min_p,i)
                max_p = max(max_p,i)

        if s.count("p") == 0 or s.count("s") == 0:
            print("YES")
            return
        
        if min_p > max_s:
            if s[0] == "." and s[-1] == ".":
                print("NO")
                return
            start = max_s - 1
            end = min_p + 1
            pot = 0
            left = 0
            while start >= 0:
                pot+=1
                start -= 1
                
            while end < n:
                left += 1
                end += 1
                

            if (left and pot):
                print("NO")
                return
            print("YES")
            return
        else:
            print("NO")
            return 
             

t = int(input())
for i in range(t):
    # if i == 56:
    #     n = input()
    #     print(input())
    #     break
    main()


        



