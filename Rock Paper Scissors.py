#  ROCK PAPER SCISSORS

import random

while True:

    def play():
        user = input("\nWhat's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            return print('It\'s a tie! Computer chose: ', computer)

        if is_win(user, computer):
            return print('You won! Computer chose: ', computer)

        return print('You lost! Computer chose: ', computer)


    def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
                or (player == 'p' and opponent == 'r'):
            return True


    play()

    play_again = input("\nIf you'd like to play again, please type 'yes'")
    if play_again == "yes":
        continue
    else:
        break
