lines = open("words.txt").readlines()
five_letters = [i for i in lines if len(i) == 6]

# for i in five_letters:
#     open("5letters.txt", "a").write(i)
# ---------------------------------------------
# five_letters = ""
# for i in lines:
#     if len(i) == 6:
#         five_letters += i
#
# open("5letters.txt", "a").write(five_letters)
# print("Done")

# ---------------------------------------------
output = "".join(five_letters)
open("5letters.txt", "a").write(output)
print("Done")
