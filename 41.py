# numbers = []
numbers = list()

for i in range(4):
    x = int(input("Enter any number : "))
    numbers.append(x)

numbers.sort()
numbers = numbers[::-1]

print(numbers)

print(max(numbers))
