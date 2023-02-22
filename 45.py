items = [
    "birdman",
    "interstellar",
    "mortal kombat",
    "matrix",
    "green mile",
    "matrix",
    "mortal kombat"]

# movies = []
#
# for i in items:
#     if i not in movies:
#         movies.append(i)

movies = list(set(items))

print(movies)
