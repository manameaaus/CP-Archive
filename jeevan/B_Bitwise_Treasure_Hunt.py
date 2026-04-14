t = int(input())
for i in range(t):
    n = int(input())
    x = bin(n)
 
    j = x[2:]
    print(j)
    # print(int(0b1001110))
    
    cc = {0}
    if n %2==0:
        cc.add(n)
    ko = 0
    bakwas = False
    if "11" in j:
        bakwas = True
    for k in range(len(j)-1,-1,-1):
        if j[k] == '1':
            n-=2**ko
            if j[k-1]=="1" or (k<len(j)-1 and j[k+1]=="1") :
                continue
            elif k>1 and (j[k-1]+j[k-2]=="00"):
                cc.add(n)
            # else:
            #     cc.add(n)
        ko+=1
        
    # or (bakwas and k<len(j)-2 and j[k-1]+j[k-2]=="01")
        
    print(len(cc))   
    print(*sorted(cc))

    

    

