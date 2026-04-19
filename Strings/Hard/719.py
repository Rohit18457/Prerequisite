def best_rotation(s):
    n = len(s)
    best = 0

    for i in range(1, n):
        for j in range(n):
            a = s[(i + j) % n]
            b = s[(best + j) % n]

            if a < b:
                best = i
                break
            elif a > b:
                break

    return best + 1

t = int(input())

for _ in range(t):
    s = input().strip()
    print(best_rotation(s))