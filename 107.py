from random import choice


def generate1():
    password = []

    for i in range(6):
        x = str(choice(range(0, 10)))
        password.append(x)

    return "".join(password)


print(generate1())
