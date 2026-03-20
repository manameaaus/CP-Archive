# t = int(input())
# for i in range(t):
#     n = int(input())
#     ans = [0] * (2*n)
#     temp = [1,2]

#     done = []
#     last = 2
#     while True:
#         if len(done) < n:
#             print("?",len(temp),*temp)
#             exp = int(input())
#             if exp == 0:
#                 last += 1
#                 temp.append(last)
#             else:
#                 ans[last-1] = exp
#                 temp.pop()
#                 done.append(last)
#                 last += 1
#                 temp.append(last)
#         else:
#             for i in range(2*n):
#                 if ans[i] == 0:
#                     print("?",n+1,done + [i+1])
#                     exp = int(input())
#                     ans[i] = exp




t = int(input())
for _ in range(t):
    n = int(input())
    ans = [0] * (2 * n)
    temp = [1, 2]

    done = []
    last = 2
    while True:
        if len(done) < n:
            print("?", len(temp), *temp, flush=True)
            exp = int(input())
            if exp == 0:
                last += 1
                temp.append(last)
            else:
                ans[last - 1] = exp
                temp.pop()
                done.append(last)
                last += 1
                temp.append(last)
        else:
            for i in range(2 * n):
                if ans[i] == 0:
                    done.append(i+1)
                    print("?", n + 1, *done, flush=True)
                    exp = int(input())
                    ans[i] = exp
                    done.pop()
            break  

    print("!", *ans, flush=True)
