class Calculator:
    def __init__(self, n1, op, n2):
        self.number1 = n1
        self.number2 = n2
        self.operator = op

    def add(self):
        print(self.number1 + self.number2)

    def subtract(self):
        print(self.number1 - self.number2)

    def multiply(self):
        print(self.number1 * self.number2)

    def divide(self):
        print(self.number1 / self.number2)


def main():
    n1 = int(input("Enter first number : "))
    op = input("Enter an operator : ")
    n2 = int(input("Enter second number : "))

    calc = Calculator(n1, op, n2)

    if op == "+":
        calc.add()
    elif op == "-":
        calc.subtract()
    elif op == "*":
        calc.multiply()
    elif op == "/":
        calc.divide()
    else:
        print("Invalid input. Try again")
        main()


main()
