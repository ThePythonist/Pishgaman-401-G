numbers = [
    10,
    8,
    5,
    3,
    13,
    14,
    21,
]

evens = []

for i in numbers:
    if i % 2 == 0:
        # evens.append(i)
        evens += [i]

print(evens)
