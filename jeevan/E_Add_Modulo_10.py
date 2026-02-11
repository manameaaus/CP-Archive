t = int(input())
for io in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    data = [i if i%2 == 0 else i + i%10 for i in l]
    mod_0 = any(i % 10 == 0 for i in data)
    data = list(set(data))
    if mod_0:
        not_same = any(i - min(data) != 0 for i in data)
        print("No" if not_same else "Yes")
    else:
        checker = set()
        for i in range(len(data)):
            num = data[i]
            while num % 10 != 2:
                num += num%10
            checker.add(num%20)
        
        print("No" if len(checker) > 1 else "Yes")





# 2 4 8 6

# 2,6,14,20
# 4,12,18,20
# 8,14,18,20
# 6,8,12,20

# or (set(d[data[i] % 10]) & set(d[prev % 10]))

