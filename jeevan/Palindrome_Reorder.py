# s = input()
# d = {}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# xx = ""
# oddc = 0
# for i in d:
#     if d[i]%2:
#         xx = i
#         oddc+=1
#     if oddc>1:
#         print("NO SOLUTION")
#         break

# if oddc<=1:
#     j = ""
#     for i in d.keys():
#         j+=i*(d[i]//2)
#     print(j,end="")
#     print(xx,end="")
#     for i in range(len(j)-1,-1,-1):
#         print(j[i],end="")


s=input()
d={} 
for elem in s:    
    if elem in d:        
        d[elem]+=1    
    else:        
        d[elem]=1 
a="" 
c=""
e=0 
for elem in d:    
    if d[elem]%2!=0:        
        e+=1        
        c+=elem       
    if e==2:            
        print("NO SOLUTION")            
        break                                  
    
if e<=1:    
    xx = ""
    for elem in d:        
               
        a+=elem*(d[elem]//2)     
    print(a+c,end="")
    for i in range (len(a)-1,-1,-1):
        xx += a[i]
        # print(a[i],end="")   
    print(xx)     
           

# s=input()
# d={}

# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# a=""
# c=""
# e=0
# for elem in d:
#     if d[elem]%2==1:
#         e+=1
#         c = elem*d[elem]
#     if e==2:
#         print("NO SOLUTION")
#         break
# if e<=1:
#     for elem in d:
#         if d[elem]%2==0:
#             a+=elem*(d[elem]//2)
#     print(a,end="")
#     print(c,end="")
#     print(a[::-1])


    

    