def initialize_table(teams):
    table = {}

    for team in teams:
        table[team] = {
            "points": 0,
            "played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0
        }

    return table

#updating table based of results (W - 3, D - 1, L - 0)
def update_table(table, home, away, result):
    if result == "H":
        table[home]["points"] += 3
        table[home]["wins"] += 1
        table[away]["losses"] += 1

    elif result == "D":
        table[home]["points"] += 1
        table[away]["points"] += 1
        table[home]["draws"] += 1
        table[away]["draws"] += 1

    else:
        table[away]["points"] += 3
        table[away]["wins"] += 1
        table[home]["losses"] += 1

    table[home]["played"] += 1
    table[away]["played"] += 1


def rank_table(table):
    return sorted(
        table.items(),
        key=lambda x: x[1]["points"],
        reverse=True
    )