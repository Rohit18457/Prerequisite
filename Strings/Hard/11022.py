import sys

memo = {}

def is_repeated(s, p):
    pattern = s[:p]
    if len(s) % p != 0:
        return False

    for i in range(0, len(s), p):
        if s[i:i+p] != pattern:
            return False
    return True


def best_weight(s):
    if s in memo:
        return memo[s]

    n = len(s)
    best = n

    # try repetition
    for p in range(1, n):
        if is_repeated(s, p):
            best = min(best, best_weight(s[:p]))
            memo[s] = best
            return best

    # try splitting
    for i in range(1, n):
        left = best_weight(s[:i])
        right = best_weight(s[i:])
        best = min(best, left + right)

    memo[s] = best
    return best


def main():
    for line in sys.stdin:
        s = line.strip()
        if s == "*":
            break
        print(best_weight(s))


main()