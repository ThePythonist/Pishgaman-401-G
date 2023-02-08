word = input("Enter any word : ")
rev_word = word[::-1]

if word == rev_word:
    print(word, "is a mirror word")
else:
    print(word, "is not a mirror word")
