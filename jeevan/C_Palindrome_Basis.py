MOD = 1e9 + 7
def check(num):
    s = str(num)
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            return False
    return True

palindromic_numbers = []
for i in range(1,40001):
    if check(i):
        palindromic_numbers.append(i)


ans = [0] * (40001)
ans[0] = 1


for temp in palindromic_numbers:
    for num in range(1,40001):
        if temp <= num:
            ans[num] = (ans[num-temp] + ans[num]) % (MOD)

t = int(input())
for i in range(t):
    n = int(input())
    print(int(ans[n]))