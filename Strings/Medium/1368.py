t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    strings = [input().strip() for _ in range(m)]

    consensus = []
    total_distance = 0

    for col in range(n):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        for row in range(m):
            count[strings[row][col]] += 1

        best_char = 'A'
        max_count = count['A']

        for ch in ['C', 'G', 'T']:
            if count[ch] > max_count:
                max_count = count[ch]
                best_char = ch

        consensus.append(best_char)
        total_distance += (m - max_count)

    print(''.join(consensus))
    print(total_distance)