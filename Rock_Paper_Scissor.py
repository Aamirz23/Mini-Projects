import random

print("---WELCOME TO ROCK PAPER SCISSORS---")

choices = ["rock", "paper","scissor"]
while True:
    user_choice = input("Enter your choice (eg. rock,paper,scissor): ").lower()

    if user_choice not in choices:
        print("Invalid input!")


    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Its a Draw!")

    elif (
            (user_choice == "rock" and computer_choice == "scissor") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissor" and computer_choice == "paper")
    ):
        print("You Win!")
    else:
        print("You Lose!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for giving your time!")
        break
    


