# number = input("Enter any number : ")
#
# try:
#     number = int(number)
#     print("It is a number")
# except ValueError:
#     print("It is not a number")
# ---------------------------------------------

# try:
#     print(x)
# except NameError or ValueError:
#     print("Tarif nashode bod")
# ---------------------------------------------

# try:
#     print(x)
# except:
#     print("Tarif nashode bod")

# ---------------------------------------------

try:
    print(x)
except Exception as error:
    print("Tarif nashode bod")
    print(error)
