# numbers = [1, 2, 3, 4, 5]
#
# for i in range(5, 10):
#     x = int(input("Enter a number between 5 and 10 :"))
#     if 5 < x <= 10:
#         numbers.append(x)
#     else:
#         print("The number is not between 5 and 10")
# print(numbers)

numbers = [1, 2, 3, 4, 5]

while len(numbers) != 10:
    n = int(input("Enter a number between 5 and 10 :"))
    if 5 < n <= 10:
        numbers.append(n)

print(numbers)
