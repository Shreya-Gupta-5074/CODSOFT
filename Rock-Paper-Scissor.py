import random

user_score = 0
computer_score = 0

while True:
    x = input("Select from rock, paper, scissor: ").lower()
    my_game = ("rock", "paper", "scissor")

    if x not in my_game:
        print("Invalid input! Please select rock, paper, scissor.\n")
        continue

    computer = random.choice(my_game)
    print("Computer selected:", computer)

    if x == computer:
        print("It's a tie!")

    elif (x == "rock" and computer == "scissor") or \
         (x == "paper" and computer == "rock") or \
         (x == "scissor" and computer == "paper"):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    # print score after every round
    print(f"\nScore → You: {user_score}  |  Computer: {computer_score}")

    # ask user if they want to play again
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again == "no":
        print("\nFinal Score:")
        print(f"You: {user_score}  |  Computer: {computer_score}")
        print("Thanks for playing!")
        break
