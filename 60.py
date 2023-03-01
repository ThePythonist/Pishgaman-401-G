word = "python"
# d = {}
#
# for i in range(len(word)):
#     d.setdefault(word[i], i)
#
# print(d)

d = dict(zip(word, range(len(word))))
print(d)
