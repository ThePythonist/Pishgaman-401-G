def check_number(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


while True:
    check_number(int(input("Enter any number : ")))

# numbers = [12, 13, 14, 15, 16]

# for i in numbers:
#     check_number(i)

# ---------------------------------------

def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_number(20))

if check_number(20) == "Even":
    print("Yes")
else:
    print("No")
