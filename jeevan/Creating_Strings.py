

# s = input()
# sasa = list(sorted(set(s.strip())))
# lensasa = len(sasa)
# lens = len(s)
# l = 10**(lens-1)
# r = l*(lensasa+1)

# yy = ""
# d = {}
# for i in range(1,lensasa+1):
#     f = str(i)
#     d[f]=sasa[i-1]
# for i in s:
#     for j in d:
#         if d[j]==i:
#             yy+=j
# hoho = sorted((yy.strip()))
# se = set()
# for i in range(l,r):
#     xx = str(i) 
#     hh = sorted((xx.strip()))
#     if hh==hoho:
#         j=""
#         for i in xx:
#            j+=d[i]
#         se.add(j)

# dfdf = sorted(se)
# print(len(dfdf))
# for i in dfdf:
#     print(i)


# s = input()
# lens = len(s)
# l = 10**(lens-1)
# r = l*(lens+1)
# yy = ""
# d = {}
# se = set()
# for i in range(1,lens+1):
#     yy+=str(i)
#     f = str(i)
#     d[f]=s[i-1]
# for i in range(l,r):
#     xx = str(i)
#     for i in yy:
#         if i not in xx:
#             break
#     else:
#         j=""
#         for i in xx:
#            j+=d[i]
#         se.add(j)
# dfdf = sorted(se)
# print(len(dfdf))
# for i in dfdf:
#     print(i)




# def create(s,d,l):
   #     if len(s)==0:
#     if s==[]:
        
#         ii=""
#         for i in sorted(d):
#             ii+=d[i]
#         if len(ii)==klkl:
#             # print(s)
#             # print(d)
#             # print(l)
#             thelod.append(ii)
#         return
#     for i in range(len(l)):
#         if l[i] not in d:

#             d[l[i]]=s[0]
#             dddr = s.pop(0)
#             gotit = l.pop(i)

#             create(s,d,l)

#             s.insert(0,dddr)
#             l.insert(i,gotit)
            
#             d={}
            





# s = input()
# so = [i for i in s]
# klkl = len(s)
# d = {}
# l = [i for i in range(len(s))]
# thelod = []
# create(so,d,l)
# print(len(thelod)*2)
# for i in sorted(thelod):
    
#     print(i)

# def create(s):
#     if s=="":
# s = input()


'''the ans'''
import copy
def pers(s,n):
   if s=="":
      return [[]]
   x = pers(s[1:],n-1)
   l = []
   for i in x:
      for j in range(n):
         h = copy.deepcopy(i)
         l.append(h)
   for i in range(len(l)):
      l[i].insert(i%(n),s[0])
   return l



s = input()
n = len(s)
so= set()
lista = sorted((pers(s,n)))
for i in lista:
   so.add("".join(i))
print(len(so))
for i in sorted(so):
   print(i)





# import copy
# def pers(s,n):
#    if s=="":
#       return [[]]
#    x = pers(s[1:],n-1)
#    l = []
#    for i in x:
#       for j in range(n):
#          h = copy.deepcopy(i)
#          l.append(h)
#    for i in range(len(l)):
#       l[i].insert(i%(n),s[0])
#    return l


# s = input()
# n = len(s)
# lista = sorted((pers(s,n)))
# print(len(lista))
# god = ["".join(i) for i in lista]
# d = {}
# for i in god:
#    if i in d:
#       d[i]+=1
#    else:
#       d[i]=1
# c = 0
# for i in d:
#    if d[i]>1:
#       print(i)
#       print(d[i])
#       c+=1
# print(c)
# print('\n\n')
# for i in god:
#    print(i)