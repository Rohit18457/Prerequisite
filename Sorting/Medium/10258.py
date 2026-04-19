tc = int(input())
input()  # blank line after test cases

for case in range(tc):

    teams = {}

    while True:
        try:
            line = input().strip()
            if line == "":
                break

            cid, prob, time, verdict = line.split()
            cid = int(cid)
            prob = int(prob)
            time = int(time)

            if cid not in teams:
                teams[cid] = {
                    "solved": 0,
                    "penalty": 0,
                    "problems": {}
                }

            team = teams[cid]

            if prob not in team["problems"]:
                team["problems"][prob] = [0, False]  # wrong, solved

            wrong, solved = team["problems"][prob]

            if solved:
                continue

            if verdict == "C":
                team["solved"] += 1
                team["penalty"] += time + wrong * 20
                team["problems"][prob][1] = True

            elif verdict == "I":
                team["problems"][prob][0] += 1

            # R, U, E are ignored automatically

        except EOFError:
            break

    result = []

    for cid in teams:
        t = teams[cid]
        result.append(( -t["solved"], t["penalty"], cid))

    result.sort()

    for solved, penalty, cid in result:
        print(cid, -solved, penalty)

    if case != tc - 1:
        print()