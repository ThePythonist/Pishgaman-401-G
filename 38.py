items = [4, 2, 5, 11, True, "Gholam", "Ekbatan", {}, 6.5]
numbers = []

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int, float]:
        numbers.append(i)

print(numbers)
