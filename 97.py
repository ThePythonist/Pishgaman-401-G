def main():
    def register():
        # username = input("Choose a username : ").lower()
        username = input("Choose a username : ").casefold()
        password = input("Choose a password : ")

        open("db-users.txt", "a+").write(username + "\n")
        open("db-passwords.txt", "a+").write(password + "\n")

        print(f"Registered user {username}")

    def login():
        db_users = [i[:-1] for i in open("db-users.txt").readlines()]
        db_passwords = [i[:-1] for i in open("db-passwords.txt").readlines()]
        accounts = dict(zip(db_users, db_passwords))

        username = input("Choose a username : ").lower()
        password = input("Choose a password : ")

        if username in accounts:
            if password == accounts[username]:
                print("Successfully logged in")
            else:
                print("Password or Username is incorrect. Try again")
                main()
        else:
            print("User not found. Try again")
            main()

    entry = input("""
Choose an option : 
1 : Register
2 : Login to your account
: """)

    if entry == "1":
        register()
    elif entry == "2":
        login()
    else:
        print("Invalid Input. Choose 1 or 2")
        main()


main()
