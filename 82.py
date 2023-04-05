# def factorial(x):
#     if x == 1:
#         # return x
#         return 1
#     else:
#         return x * factorial(x - 1)


factorial = lambda x: x if x == 1 else x * factorial(x - 1)
number = int(input("Enter any number to see the factorial : "))
print(factorial(number))
