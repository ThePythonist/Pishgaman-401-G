person = {
    "name": "navid mohammadzadeh",
    "job": "actor",
    "age": 30,
    "city": "kurdestan"
}

key = input("Enter any key to search : ")

if key in person.keys():
    print("Found :", person[key])
else:
    print("Not Found")
