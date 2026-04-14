import sys

def flush():
    sys.stdout.flush()

def read_int():
    val = int(input())
    if val == -1:
        sys.exit()
    return val

def solve_case(n):
    path_lengths = {}
    for x in range(1, n + 1):
        S = [i for i in range(1, n + 1) ]
        print(f"? {x} {len(S)} {' '.join(map(str, S))}")
        flush()
        r = read_int()
        path_lengths[x] = r

    max_len = max(path_lengths.values())
    start_node = next(k for k, v in path_lengths.items() if v == max_len)

    ans = [start_node]
    current_len = max_len

    while current_len > 1:
        for v in path_lengths:
            if path_lengths[v] == current_len - 1:
                print(f"? {ans[-1]} 2 {' '.join(map(str, [v,ans[-1]]))}")
                flush()
                r = read_int()
                if r == 2:
                    ans.append(v)
                    current_len -= 1
                    break

    print(f"! {len(ans)} {' '.join(map(str, ans))}")
    flush()

def main():
    t = read_int()
    for _ in range(t):
        n = read_int()
        solve_case(n)

if __name__ == "__main__":
    main()
