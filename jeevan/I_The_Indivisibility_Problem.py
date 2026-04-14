n = int(input())

res = 0
res += n//2
res += n//3
res += n//5
res += n//7


res -= n//(2 * 3)
res -= n//(2 * 5)
res -= n//(2 * 7)

res -= n//(3 * 5)
res -= n//(3 * 7)

res -= n//(5 * 7)


res += n//(2 * 3 * 5)
res += n//(2 * 3 * 7)
res += n//(2 * 5 * 7)
res += n//(3 * 5 * 7)


res -= n//(2 * 3 * 5 * 7)


print(n-res)