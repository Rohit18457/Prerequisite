import sys

arr = []

for line in sys.stdin:
    num = int(line.strip())
    arr.append(num)
    arr.sort()
    
    n = len(arr)
    
    if n % 2 == 1:
        print(arr[n // 2])
    else:
        mid1 = arr[n // 2]
        mid2 = arr[n // 2 - 1]
        print((mid1 + mid2) // 2)