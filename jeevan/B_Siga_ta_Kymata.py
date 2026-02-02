import bisect

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    s = input().strip()

    # Build prefix list: (value, index), sorted
    prefix = []
    # Build suffix list: (value, -index)
    suffix = [(arr[i], -i) for i in range(n)]
    suffix.sort()  # ascending by value, -index

    results = []

    for i in range(n):
        # Remove current element from suffix
        idx_in_suffix = bisect.bisect_left(suffix, (arr[i], -i))
        if idx_in_suffix < len(suffix) and suffix[idx_in_suffix] == (arr[i], -i):
            suffix.pop(idx_in_suffix)

        if s[i] == '1':
            # ===== Prefix: find largest value < arr[i] =====
            pos = bisect.bisect_left(prefix, (arr[i], -1))  # first >= arr[i]
            if pos > 0:
                prefix_idx = prefix[0:pos][0][1]  # smallest index among values < arr[i]
            else:
                prefix_idx = -1

            # ===== Suffix: find first value > arr[i] =====
            print(suffix)
            pos = bisect.bisect_right(suffix, (arr[i], -n))  # first element > arr[i]
            if pos < len(suffix):
                suffix_idx = -suffix[pos][1]  # convert back to positive index
            else:
                suffix_idx = -1

            results.append((i, prefix_idx, suffix_idx))

        # Insert current element into prefix in sorted order
        bisect.insort(prefix, (arr[i], i))

    # Print results
    print("arr:", arr)
    for i, p, q in results:
        print(f"i={i}, prefix_idx={p}, suffix_idx={q}")

    # print(suffix)

# Example usage
if __name__ == "__main__":
    solve()

