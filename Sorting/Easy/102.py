while True:
    try:
        b1,g1,c1,b2,g2,c2,b3,g3,c3 = map(int,input().split())
        
        ans = []
        
        ans.append(("BCG", g1+c1 + b2+g2 + b3+c3))
        ans.append(("BGC", g1+c1 + b2+c2 + b3+g3))
        ans.append(("CBG", b1+g1 + c2+g2 + b3+c3))
        ans.append(("CGB", b1+g1 + b2+c2 + g3+b3))
        ans.append(("GBC", b1+c1 + g2+c2 + g3+b3))
        ans.append(("GCB", b1+c1 + b2+g2 + c3+g3))
        
        ans.sort(key=lambda x: (x[1], x[0]))
        
        print(ans[0][0], ans[0][1])
        
    except:
        break