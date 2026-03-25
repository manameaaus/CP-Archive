t = int(input())
for i in range(t):
    s = input()
    j = s[::-1]
    for i in j:
        if i=="p":
            print("q",end="")
        elif i=="q":
            print("p",end="")
        else:
            print(i,end="")
    print()