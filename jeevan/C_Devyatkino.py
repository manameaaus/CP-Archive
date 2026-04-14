def nine(x,lina):
    xx = lina - x
    return int("9"*xx)

def fun(n,lina):
    priority = [8,9,0,1,2,3,4,5,6]
    s = str(n)
    mina = 11
    for i in range(lina):
        if priority.index(int(s[i])) <= mina:
            mina = priority.index(int(s[i])) 
            ans = i
    return ans

def addup(no,num):
    return no + num
   

t = int(input())

for i in range(t):
    n = int(input())
    lina = len(str(n))
    c = 0
    while True:
        # fun(n,lina)
        if "7" in str(n):
            print(c)
            break
        else:
            idx = fun(n,len(str(n)))
            print(idx)
            nona = nine(idx,len(str(n)))
            print(nona)
            n = addup(nona,n)
            print(n)
            print()
            c += 1

# 11,11,137
# 15 + 99 + 999 +9999 + 99999 +999999 + 9 +9+9