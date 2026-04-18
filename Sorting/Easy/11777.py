t = int(input())

for i in range(1, t+1):
    t1, t2, final, att, ct1, ct2, ct3 = map(int, input().split())
    
    # best two CTs
    cts = [ct1, ct2, ct3]
    cts.sort(reverse=True)
    ct_avg = (cts[0] + cts[1]) // 2
    
    total = t1 + t2 + final + att + ct_avg
    
    if total >= 90:
        grade = 'A'
    elif total >= 80:
        grade = 'B'
    elif total >= 70:
        grade = 'C'
    elif total >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"Case {i}: {grade}")