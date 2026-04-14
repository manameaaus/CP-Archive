num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

nee = 0
jee = 0

for i in range(len(num1)):
    nee ^= num1[i]

for i in range(len(num2)):
    jee ^= num2[i]

if len(num1) % 2 == 0 and len(num2) % 2 == 0:
    print(0)

elif len(num2) % 2 == 0:
    print(jee)

elif len(num1) % 2 == 0:
    print(nee)

else:
    print(nee^jee)