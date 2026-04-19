def smallest_period(s):
    n = len(s)
    lps = [0] * n
    j = 0

    # Build LPS array
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]
        if s[i] == s[j]:
            j += 1
            lps[i] = j

    k = n - lps[-1]

    if n % k == 0:
        return k
    return n


t = int(input())
input()  # blank line

for i in range(t):
    s = input().strip()
    print(smallest_period(s))

    if i != t - 1:
        print()
        input()  # skip blank line