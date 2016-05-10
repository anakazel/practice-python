from random import randint

print("Welcome to Guess-The-Number!")
generated_number = randint(1, 9)
while True:
    user_input = int(input("Your guess ?"))
    if user_input == 'exit':
        break
    if user_input == generated_number:
        if input("You found the number! Type 'exit' to end the game.") == 'exit':
            break
    elif user_input < generated_number:
        print("Too low!")
    else:
        print("Too high!")
