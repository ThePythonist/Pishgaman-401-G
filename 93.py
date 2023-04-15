# lines = open("words.txt").readlines()
# items = [i[0:-1] for i in lines]
# print(items)


lines = open("words.txt").read().split("\n")
print(lines)
