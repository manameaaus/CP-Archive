n = int(input())
s = input()
if n<26:
    print("NO")
else:
    s = s.lower()
    j = "qwertyuiopasdfghjklzxcvbnm"
    ans="YES"
    for i in j:
        if i not in s:
            ans = "NO"
            break
    print(ans)
    