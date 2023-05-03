from random import choice

number = choice(range(0, 11))
chances = 5

print("Welcome to number guessing game ")

while chances > 0:
    print(f"You have {chances} chances left")
    guess = input("Guess the number : ")

    try:
        guess = int(guess)
        if guess > 0:
            if guess == number:
                print("You won!")
                break
            elif guess > number:
                print("Try smaller than", guess)
            else:
                print("Try bigger than", guess)
            chances -= 1
        else:
            print("Your must be between 0-10")
    except ValueError:
        print("Your guess must be a number. Try again")

if chances == 0:
    print("Game over! The number was :", number)
