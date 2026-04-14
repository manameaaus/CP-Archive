import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    st = 10 ** 3
    while True:
        while st > 0:
            print(f"add -{st}")
            sys.stdout.flush()
            res = sys.stdin.readline().strip()
            if res == "0":
                st //= 10
        print(f"add {n-1}")
        sys.stdout.flush()
        res = sys.stdin.readline().strip()
        print("!")
        sys.stdout.flush()
        res = sys.stdin.readline().strip()
        # if res == "!":
        break
# print("cjwcnwjd")

            
