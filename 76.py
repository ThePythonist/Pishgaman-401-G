def main():
    def factorial(x):
        if x == 1:
            # return x
            return 1
        else:
            return x * factorial(x - 1)

    entry = input("Enter any number to see the factorial : ")

    # if entry > 0:
    #     print(factorial(entry))
    # elif entry == 0:
    #     print("Factorial of 0 is 1")
    # else:
    #     print("Factorial doesn't exist")
    #

    try:
        entry = int(entry)
        try:
            print("Factorial is :", factorial(entry))
        except RecursionError as error:
            print(error)
            main()
    except ValueError:
        print("Entry must be number. Try again")
        main()


main()
