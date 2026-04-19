import sys

def lcs(A, B):
    n, m = len(A), len(B)

    # dp[i][j] = LCS string of A[:i], B[:j]
    dp = [[""] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):

            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + " " + A[i] if dp[i][j] else A[i]

            else:
                # choose longer sequence
                if len(dp[i][j + 1].split()) > len(dp[i + 1][j].split()):
                    dp[i + 1][j + 1] = dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]

    return dp[n][m]


lines = sys.stdin.read().strip().split("\n")
i = 0
n = len(lines)

while i < n:
    A = []
    B = []

    # first text
    while i < n and lines[i] != "#":
        A += lines[i].split()
        i += 1

    i += 1  # skip #

    # second text
    while i < n and lines[i] != "#":
        B += lines[i].split()
        i += 1

    i += 1  # skip #

    if A and B:
        print(lcs(A, B))