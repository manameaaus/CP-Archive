t = int(input())
for i in range(t):
    n = int(input())
    l = list(input())
    stack = []
    allot = False
    back = -1
    front = -1
    ans = [0] * n
    for i in range(n):
        if not stack or stack[-1][0] == l[i]:
            stack.append([l[i],i])
        else:
            if not allot:
                if l[i] == '(':
                    back = 1
                    front = 2
                else:
                    front = 1
                    back = 2
                allot = True

            if l[i] == '(':
                ans[i] = back
                ans[stack[-1][1]] = back
            else:
                ans[i] = front
                ans[stack[-1][1]] = front

            stack.pop()

    if stack:
        print(-1)
    else:
        print(max(ans))
        print(*ans)

