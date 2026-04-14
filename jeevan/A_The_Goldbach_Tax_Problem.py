def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        if i * i >= n:
            return True




n = int(input())
if n%2 == 0:
    if n == 2:
        print(1)
    else:
        print(2)
else:
    if (isPrime(n)):
        print(1)
    elif(isPrime(n-2)):
        print(2)
    else:
        print(3)