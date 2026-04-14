n = int(input())
numbers = list(map(int, input().split()))

count = {i:0 for i in range(1, 8)}
for i in numbers:
    count[i] += 1
result = []

while count[1] > 0:
    if count[2] > 0 and count[4] > 0:
        result.append((1, 2, 4))
        count[1] -= 1
        count[2] -= 1
        count[4] -= 1
    elif count[2] > 0 and count[6] > 0:
        result.append((1, 2, 6))
        count[1] -= 1
        count[2] -= 1
        count[6] -= 1
    elif count[3] > 0 and count[6] > 0:
        result.append((1, 3, 6))
        count[1] -= 1
        count[3] -= 1
        count[6] -= 1
    else:
        break

if any(count.values()):
    print(-1)
else:
    for group in result:
        print(*group)


