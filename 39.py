items = [4, 2, 5, 11, True, "Gholam", "Ekbatan", {}, 6.5]
words = []

for i in items:
    if type(i) == str:
        words.append(i)

print(words)
