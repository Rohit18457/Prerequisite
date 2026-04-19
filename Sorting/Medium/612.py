import sys

def count_inv(s):
    inv = 0
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] > s[j]:
                inv += 1
    return inv


input = sys.stdin.readline

m = int(input())
input()

for t in range(m):
    n, k = map(int, input().split())
    arr = []

    for i in range(k):
        s = input().strip()
        arr.append((count_inv(s), i, s))

    arr.sort()

    for item in arr:
        print(item[2])

    if t != m - 1:
        print()