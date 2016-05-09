
def is_valid_option(input):
    return input == 'r' or input == 'p' or input == 's'

print("Welcome to Rock-Paper-Scissors game!")

player1_name = input("Player 1, what is your name ?")
print("Nice to meet you, " + player1_name + ".")
player2_name = input("Player 2, what is your name ?")
print("Nice to meet you, " + player2_name + ".")

while True:
    player1_answer = input(player1_name + " what do you want to choose ?\nPress 'r' for rock 's' for scissors 'p' for paper.")
    if is_valid_option(player1_answer) == False:
        print("Invalid option.")
    player2_answer = input(player2_name + " what do you want to choose ?\nPress 'r' for rock 's' for scissors 'p' for paper.")
    if is_valid_option(player2_answer) == False:
        print("Invalid option.")
    else:
        winners = {'r' : 0, 's' : 1, 'p': 2}
        player1_answer_index = winners.get(player1_answer)
        player2_answer_index = winners.get(player2_answer)
        difference = player1_answer_index - player2_answer_index

        if difference in [-1, 2]:
            print("Player " + player1_name + " won!")
            if str(input("Do you want to play another game? [y/n]")) == 'y':
                continue
            else:
                print("Game over!")
                break;
        elif difference in [-2, 1]:
            print("Player " + player2_name + " won!")
            if str(input("Do you want to play another game? [y/n]")) == 'y':
                continue
            else:
                print("Game over!")
                break;
        else:#difference is 0
            print("Tie! Please continue playing.")









