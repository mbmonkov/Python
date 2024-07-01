def movie_organizer(*args):
    collection = {}
    for movie_name, genre in args:
        if genre not in collection:
            collection[genre] = []
        collection[genre].append(movie_name)

    result = ""
    for genre, movies in sorted(collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies):
            result += f"* {movie}\n"
    return result

