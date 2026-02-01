import random
import sys
t = int(input())
for i in range(t):
    n = int(input())
    p = 1
    q = 2
    r = 3
    while True:
        print("?",p,q,r)
        sys.stdout.flush()
        k = int(input())
        if k == 0:
            print("!",p,q,r)
            break
        
        j = random.randint(1,3)
        if j == 1:
            p = k
        elif j == 2:
            q = k
        else:
            r = k 
        
