from random import randint

print("Welcome to Guess-The-Number!")
MIN = 1
MAX = 9
generated_number = randint(MIN, MAX)
tries = 0

while True:
    user_input = int(input("Your guess ?"))
    tries += 1
    if user_input == 'exit':
        break
    if user_input == generated_number:
        if input("You found the number in " + str(tries) + " tries! Type 'exit' to end the game.") == 'exit':
            break
        else:
            continue
    elif user_input < generated_number:
        print("Too low!")
    else:
        print("Too high!")
