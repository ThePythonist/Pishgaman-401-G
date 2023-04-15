lines = open("words.txt").readlines()
# five_letters = []

# for line in lines :
#     if len(line) == 6 :
#         five_letters.append(line)

five_letters = [ i for i in lines if len(i) == 6]
print(five_letters)
