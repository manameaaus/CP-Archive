# t = int(input())
# import math
# for i in range(t):
#     n = int(input())
#     x = n//26
#     bot = (((1 + 8 * x)**(0.5) - 1)//2)
#     top = n - ((bot * (bot + 1)) / 2) * 26
#     print(chr(math.ceil(top/(bot+1)) + 96))

# print(26 * (((196116136 * 196116136) + 196116136)/2))


t = int(input())
import math
for i in range(t):
    n = int(input())
    bot = (((1 + 8 * n//26)**(0.5) - 1)//2)
    rem = n - ((bot * (bot + 1)) / 2) * 26

    if rem:
        print(chr(math.ceil(rem/(bot+1)) + 96))
    else:
        print("z")
    