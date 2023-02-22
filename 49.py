number = int(input("Enter any number to check if it is prime : "))
divisors = [i for i in range(1, number + 1) if number % i == 0]

# if divisors == [1, number]:
if len(divisors) == 2:
    print("The number is prime")
else:
    print("The number is not prime")
