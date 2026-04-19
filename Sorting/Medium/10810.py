import sys
sys.setrecursionlimit(10**7)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    inv = inv_left + inv_right

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv


while True:
    line = sys.stdin.readline().strip()
    if not line:
        break

    n = int(line)
    if n == 0:
        break

    arr = [int(sys.stdin.readline()) for _ in range(n)]

    _, inv = merge_sort(arr)
    print(inv)