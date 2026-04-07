b,g = map(int,input().split())
if b>g:
    start  = "B"
    end = "G"
    l = g
    h = b
else:
    start = "G"
    end = "B"
    l = b
    h = g
print((start+end)*l + start*(h-l))