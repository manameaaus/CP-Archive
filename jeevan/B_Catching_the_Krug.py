t = int(input())
for i in range(t):
    n,x1,y1,x2,y2 = map(int,input().split())
    

    dist_x = abs(x2-x1)
    dist_y = abs(y2-y1)

    mina = max(dist_x,dist_y)
    

    ans = mina
    bound_right = min(n,x2+mina)
    bound_left = max(0,x2-mina)
    bound_top = max(0,y2-mina)
    bound_bottom = min(n,y2+mina)

    if x1 + mina > bound_right:
        ans = max(ans,mina + n - bound_right)
    if x1 - mina < bound_left:
        ans = max(ans,mina + bound_left)
    if y1 + mina > bound_bottom:
        ans = max(ans,mina + n - bound_bottom)
    if y1 - mina < bound_top:
        ans = max(ans,mina + bound_top)


    print(ans)