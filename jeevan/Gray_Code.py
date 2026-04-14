# n = int(input())
# lis=[]
# for i in range(2**n):
#     b = ((bin(i).split('0b')[1]))
#     sss = len(str(b))
#     lis.append("0"*(n-sss)+b)
# for i in lis:
#     print(i)


'''1st method'''

# n = int(input())
# po = 2**n
# lis = []
# for i in range(po):
#     x = [0]*n
#     lis.append(x)
# for i in range(1,n+1):
#     for j in range(2**(i-1),po,2**(i+1)):
#         for k in range(2**i):
#             if j+k<po:
#                 lis[j+k][-1*i] = 1
# for i in lis:
#     for j in i:
#         print(j,end="")
#     print()


'''2nd method'''
# n = int(input())
# l = ["0","1"]
# for i in range(n-1):
#     l+=l[::-1]

#     for i in range(len(l)//2):
#         l[i]= "0"+l[i]
#     for i in range(len(l)//2,len(l)):
#         l[i]= "1"+l[i]
    
# for i in l:
#     print(i)

'''2.1th method'''
# def pat(n):
#     if n==1:
#         return ["0","1"]
#     l = pat(n-1)
#     l+=l[::-1]
#     for i in range(len(l)//2):
#         l[i]="0"+l[i]
#     for i in range(len(l)//2,len(l)):
#         l[i]="1"+l[i]
#     return l


# n = int(input())
# c = pat(n)
# for i in c:
#     print(i)



       
        
              

