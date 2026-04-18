import bisect

while True:
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        break
    
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    q = int(input())
    
    for _ in range(q):
        L, U = map(int, input().split())
        max_size = 0
        
        for i in range(n):
            j = bisect.bisect_left(mat[i], L)
            
            size = max_size
            while i + size < n and j + size < m and mat[i + size][j + size] <= U:
                size += 1
            
            max_size = max(max_size, size)
        
        print(max_size)
    
    print("-")