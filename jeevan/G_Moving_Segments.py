def merge(a,b):
    nee = 0
    for k in range(1,min(len(a),len(b))+1):
        if a[-k:] == b[:k]:
            nee = k
    
    return a+b[nee:]

a = input()
b = input()

print(merge(a,b))
print(merge(b,a))
print(merge(a[::-1],b))
print(merge(b,a[::-1]))