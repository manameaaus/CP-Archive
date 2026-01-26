n,x = map(int,input().split())
l = list(map(int,input().split()))
freq = [0] * (x + 1)
for num in l:
    freq[num] += 1

for i in range(1,x):
    if freq[i] % (i+1):
        print("No")
        break
    freq[i+1] += freq[i] // (i+1)
else:
    print("Yes")



