import sys

while True:
    n, m = map(int, input().split())
    
    print(n, m)
    
    if n == 0 and m == 0:
        break
    
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    
    def custom_sort(x):
        return (x % m, 
                0 if x % 2 != 0 else 1, 
                -x if x % 2 != 0 else x)
    
    arr.sort(key=custom_sort)
    
    for num in arr:
        print(num)