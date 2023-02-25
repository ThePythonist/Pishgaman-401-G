numbers = []

for i in range(3):
    entry = input("Entry : ")

    try:
        entry = float(entry)
        print("inja :",entry)
        if str(entry)[-2:] == ".0":
            numbers.append(int(entry))
        else :
            numbers.append(entry)
    except ValueError:
        # print(entry, "Was not a number")
        pass

print("Numbers :", numbers)
