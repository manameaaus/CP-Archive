k = input()
s = (input())
if len(k)==len(s):
    j=""
    for i in range(len(s)-1,-1,-1):
        j+=s[i]
    if j==k:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
