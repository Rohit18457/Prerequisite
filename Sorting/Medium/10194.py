import sys

def process_tournament(name, teams, games):
    stats = {}

    for t in teams:
        stats[t] = {
            "points": 0,
            "played": 0,
            "wins": 0,
            "ties": 0,
            "losses": 0,
            "gf": 0,
            "ga": 0
        }

    for g in games:
        left, right = g.split("#")
        team1 = left
        mid = right.split("#")
        goals1 = int(mid[0].split("@")[0])
        goals2 = int(mid[0].split("@")[1])
        team2 = mid[1]

        stats[team1]["played"] += 1
        stats[team2]["played"] += 1

        stats[team1]["gf"] += goals1
        stats[team1]["ga"] += goals2
        stats[team2]["gf"] += goals2
        stats[team2]["ga"] += goals1

        if goals1 > goals2:
            stats[team1]["wins"] += 1
            stats[team2]["losses"] += 1
            stats[team1]["points"] += 3
        elif goals1 < goals2:
            stats[team2]["wins"] += 1
            stats[team1]["losses"] += 1
            stats[team2]["points"] += 3
        else:
            stats[team1]["ties"] += 1
            stats[team2]["ties"] += 1
            stats[team1]["points"] += 1
            stats[team2]["points"] += 1

    def sort_key(item):
        team, s = item
        return (
            -s["points"],
            -s["wins"],
            -(s["gf"] - s["ga"]),
            -s["gf"],
            s["played"],
            team.lower(),
            team
        )

    ranked = sorted(stats.items(), key=sort_key)

    print(name)
    for i, (team, s) in enumerate(ranked, 1):
        gd = s["gf"] - s["ga"]
        print(f"{i}) {team} {s['points']}p, {s['played']}g "
              f"({s['wins']}-{s['ties']}-{s['losses']}),"
              f"{gd}gd ({s['gf']}-{s['ga']})")


def main():
    input_data = sys.stdin.read().strip().split("\n")
    idx = 0
    n = int(input_data[idx]); idx += 1

    out = []

    for _ in range(n):
        tour_name = input_data[idx]; idx += 1
        t = int(input_data[idx]); idx += 1

        teams = []
        for _ in range(t):
            teams.append(input_data[idx])
            idx += 1

        g = int(input_data[idx]); idx += 1

        games = []
        for _ in range(g):
            games.append(input_data[idx])
            idx += 1

        stats = {}

        for team in teams:
            stats[team] = {
                "points": 0, "played": 0, "wins": 0,
                "ties": 0, "losses": 0, "gf": 0, "ga": 0
            }

        for line in games:
            t1, rest = line.split("#")
            g1, rest = rest.split("@")
            g2, t2 = rest.split("#")
            g1 = int(g1)
            g2 = int(g2)

            stats[t1]["played"] += 1
            stats[t2]["played"] += 1

            stats[t1]["gf"] += g1
            stats[t1]["ga"] += g2
            stats[t2]["gf"] += g2
            stats[t2]["ga"] += g1

            if g1 > g2:
                stats[t1]["wins"] += 1
                stats[t2]["losses"] += 1
                stats[t1]["points"] += 3
            elif g1 < g2:
                stats[t2]["wins"] += 1
                stats[t1]["losses"] += 1
                stats[t2]["points"] += 3
            else:
                stats[t1]["ties"] += 1
                stats[t2]["ties"] += 1
                stats[t1]["points"] += 1
                stats[t2]["points"] += 1

        def key(item):
            team, s = item
            return (
                -s["points"],
                -s["wins"],
                -(s["gf"] - s["ga"]),
                -s["gf"],
                s["played"],
                team.lower(),
                team
            )

        ranked = sorted(stats.items(), key=key)

        print(tour_name)
        for i, (team, s) in enumerate(ranked, 1):
            gd = s["gf"] - s["ga"]
            print(f"{i}) {team} {s['points']}p, {s['played']}g "
                  f"({s['wins']}-{s['ties']}-{s['losses']}),"
                  f"{gd}gd ({s['gf']}-{s['ga']})")

        n -= 1
        if _ != n:
            print()


if __name__ == "__main__":
    main()