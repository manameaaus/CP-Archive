def find101(a):
    n = len(a)
    res = []

    idx = 0
    while (idx < n):
        if a[idx] != 1:
            idx += 1
        else:
            nee = [idx]
            idx += 1
            while (idx < n):
                if a[idx] == 0:
                    idx += 1
                elif a[idx] == 1:
                    nee.append(idx)
                    res.append(nee)
                    break
                else:
                    break

    return res

def find102(a):
    n = len(a)
    res = []

    idx = 0
    while (idx < n):
        if a[idx] != 1:
            idx += 1
        else:
            nee = [idx]
            idx += 1
            while (idx < n):
                if a[idx] == 0:
                    idx += 1
                elif a[idx] == 2:
                    nee.append(idx)
                    res.append(nee)
                    break
                else:
                    break

    return res

def find201(a):
    n = len(a)
    res = []

    idx = 0
    while (idx < n):
        if a[idx] != 2:
            idx += 1
        else:
            nee = [idx]
            idx += 1
            while (idx < n):
                if a[idx] == 0:
                    idx += 1
                elif a[idx] == 1:
                    nee.append(idx)
                    res.append(nee)
                    break
                else:
                    break

    return res


t = 1

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ids = []
    res = 0

    ids.extend(find201(a))
    ids.extend(find102(a))
    ids.extend(find101(a))

    for i, j in ids:
        ll = abs(j-i+1)

        cur = 0

        if ll > 2:
            cur = 1
        
        l = i-1
        r = j+1 

        rght = 0
        left = 0

        while l >= 0 and a[l] == 0:
            rght += 1
            l -= 1
        
        while r < n and a[r] == 0:
            left += 1
            r += 1

        if cur:
            res += (rght+1)*(left+1)
        else:
            res += (rght+1)*(left+1)-1
            # print(rght, left)
    
    # print(ids)
    print(res)