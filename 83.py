# def check(word):
#     if len(word) == len(set(word)):
#         print("Tekrari nadarad")
#     else:
#         print("Tekrari darad")


check = lambda word: True if len(word) == len(set(word)) else False
print(check(input("Enter any word to check if it is pangram : ")))
