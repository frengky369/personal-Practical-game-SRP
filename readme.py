#11 Scissors-Rock-Paper
import random

user_win = 0
com_win = 0

while True:
    # play 3 round
    round_counter = 0
    user_win = 0
    com_win = 0

    while round_counter < 3:
        print("0: scissors, 1: rock, and 2: paper")

        user_choice = int(input("Enter your choice: "))
        com_choice = random.randint(0, 2)

        # Output computer choice
        if com_choice == 0:
            print("Computer's choice: Scissors")
        elif com_choice == 1:
            print("Computer's choice: Rock")
        else:
            print("Computer's choice: Paper")

        # win or lose
        if user_choice == com_choice:
            print("Draw!")
        elif (user_choice == 0 and com_choice == 2) or \
             (user_choice == 1 and com_choice == 0) or \
             (user_choice == 2 and com_choice == 1):
            print("You win!")
            user_win += 1
        else:
            print("You lose!")
            com_win += 1

        round_counter += 1
        print()

    # 3 round result
    print("You won", user_win, "time and computer won", com_win, "times")

    # final winner
    if user_win > com_win:
        print("You are the final winner!")
        break
    elif com_win > user_win:
        print("Computer is the final winner!")
        break
    else:
        print("No winner, continue for another round...\n")

