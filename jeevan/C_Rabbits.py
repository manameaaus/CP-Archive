def main():
    n = int(input())
    s = [i for i in input()]

    new = []

    curr = s[0]
    c = 0

    for i in s:
        if i == curr:
            c += 1
        else:
            new.append(curr)
            if c > 1:
                new.append(curr)
            curr = i
            c = 1

    new.append(curr)
    if c > 1:
        new.append(curr)

    test = "".join(new)
    kot = test.split("11")

    for i in range(len(kot)):
        if "00" in kot[i] or kot[i].count("0") % 2 == 0 or (i == 0 and kot[i][0] == "0") or (i == len(kot)-1 and kot[i][-1] == "0"):
            continue
        else:
            print("NO")
            return
        
    print("YES")

t = int(input())
for i in range(t):
    main()



    # if ("11011" in test) or ("a1011" in "a"+test) or ("1101a" in test+"a"):
    #     print("NO")
    #     return
