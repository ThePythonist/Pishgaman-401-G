integer = int(input('Integer part : '))
decimal = int(input('Decimal part : '))

# print(f"{integer}.{decimal}")
output = float("{i}.{d}".format(d=decimal, i=integer))
print(output)
print(type(output))