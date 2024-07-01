def team_lineup(*args):
    collection = {}
    for name, country in args:
        if country not in collection:
            collection[country] = []
        collection[country].append(name)
    result = []

    sorted_col = dict(sorted(collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    for country, name in sorted_col.items():
        result.append(f"{country}:")
        for cur_name in name:
            result.append(f"  -{cur_name}")
    return '\n'.join(result)




print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
