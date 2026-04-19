import sys

def max_power(s):
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

    # Length of smallest repeating unit
    length = n - lps[-1]

    if n % length == 0:
        return n // length
    return 1


for line in sys.stdin:
    s = line.strip()
    if s == ".":
        break
    print(max_power(s))