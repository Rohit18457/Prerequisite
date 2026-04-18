t = int(input())
people = []

for _ in range(t):
    dept = input()
    
    while True:
        try:
            line = input()
            if line == "":
                break
            
            data = line.split(',')
            title, fname, lname = data[0], data[1], data[2]
            
            people.append((lname, title, fname, dept, data))
        
        except:
            break

people.sort(key=lambda x: x[0])

for p in people:
    lname, title, fname, dept, data = p
    
    print("----------------------------------------")
    print(f"{title} {fname} {lname}")
    print(data[3])
    print(dept)
    print(f"Home Phone: {data[4]}")
    print(f"Work Phone: {data[5]}")
    print(f"Campus Box: {data[6]}")