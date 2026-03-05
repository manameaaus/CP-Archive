t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    i = 0
    extra = set()
    new = set()
    st = 0
    
    while i < n:
        if len(extra) == 0:
            extra.add(a[i])
        else:
            while i < n:
                if a[i] in extra:
                    extra.remove(a[i])
                new.add(a[i])
                if len(extra) == 0:
                    extra = new
                    new = set()
                    st += 1
                    break
                i += 1
        i += 1
    print(st+1)