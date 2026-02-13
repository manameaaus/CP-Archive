def build(ind,st,end):
    if st == end:
        seg[ind] = arr[st]
        return seg[ind]
    mid = (st+end) // 2
    seg[ind] = build(ind*2,st,mid) + build(ind*2+1,mid+1,end)
    return seg[ind]


def update(ind,st,end,kaha,naya):
    if st == end:
        arr[kaha] = naya
        seg[ind] = arr[kaha]
        return

    mid = (st+end) // 2

    if kaha <= mid:
        update(2*ind,st,mid,kaha,naya)
    else:
        update(2*ind+1,mid+1,end,kaha,naya)

    seg[ind] = seg[ind*2] + seg[ind*2+1]
    

def query(ind,st,end,l,r):
    if end < l or st > r:
        return 0
    
    if st >= l and r >= end:
        return seg[ind]

    mid = (st+end) // 2
    return (query(2*ind,st,mid,l,r) + query(2*ind + 1,mid+1,end,l,r))

n,q = map(int,input().split())
arr = [0] * (n+1)
seg = [0] * (4*n)
build(1,1,n)

for i in range(q):
    lis = list(input().split())
    lis[1] = int(lis[1])
    lis[2] = int(lis[2])
    if lis[0] == 'A':
        update(1,1,n,lis[1],lis[2])
    else:
        print(query(1,1,n,lis[1],lis[2]))




