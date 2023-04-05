# def f1(text):
#     words = text.split()
#     lengths = []
#
#     for i in words:
#         lengths.append(len(i))
#
#     longest = max(lengths)
#
#     for i in words:
#         if len(i) == longest:
#             return i
#
#
# text = "Python is a good programming language"
# print(f1(text))


# def f2(text):
#     words = text.split()
#     words.sort(key=len)
#     return words[-1]
#
#
# text = "Python is a good programming language"
# print(f2(text))


def f3(text):
    words = text.split()
    # return min(words, key=len)
    return max(words, key=len)


text = "Python is a good programming language"
print(f3(text))
