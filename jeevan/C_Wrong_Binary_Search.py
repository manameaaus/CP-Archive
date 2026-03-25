def main():
    n = int(input())
    s = input()
    arr = list(s)
    ans = [i+1 for i in range(n)]

    if ("a01" in "a" + s) or ("10a" in s + "a") or ("101" in s):
        print("NO")
        return
        
    for i in range(1,n):
        if arr[i] == "0" and arr[i-1] != "1":
            ans[i],ans[i-1] = ans[i-1],ans[i]

    print("YES")
    print(*ans)

t = int(input())
for i in range(t):
    main()