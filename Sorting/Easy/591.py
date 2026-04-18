set_num = 1

while True:
    n = int(input())
    
    if n == 0:
        break
    
    arr = list(map(int, input().split()))
    
    avg = sum(arr) // n
    
    moves = 0
    for h in arr:
        if h > avg:
            moves += (h - avg)
    
    print(f"Set #{set_num}")
    print(f"The minimum number of moves is {moves}.\n")
    
    set_num += 1