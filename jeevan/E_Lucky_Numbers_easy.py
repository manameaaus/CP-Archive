def recur(n,pot):
    if n == 0:
        # se.add(pot)
        return
    
    se.add(pot)
    recur(n-1,(pot*10)+4)
    recur(n-1,(pot*10)+7)

a = int(input())
se = set()
recur(13,0)

for i in sorted(se):
    if i >= a and str(i).count('7') == str(i).count('4'):
        print(i)
        break



