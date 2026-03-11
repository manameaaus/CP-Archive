t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    under = s.count("_")
    dash = s.count("-")
    if dash%2==0:
        print(int((dash/2)**2 * (under)))
    else:
        print(int((dash//2) * ((dash//2)+1) * under))