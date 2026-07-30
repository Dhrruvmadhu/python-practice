import random

name = input("Enter your Name:")
print(f"Hello {name}, let's play this game")

print(f"so {name}, You have a three choices you need to select one from ")
print("Stone , Paper , Scissors")


def game():
    player = input("Enter your choice: ").lower()
    computer = random.choice(["stone", "paper", "scissors"])

    print(f"Player choose: {player} ")
    print(f"computer choose: {computer}")

    if player == computer:
        print("It's a Draw!!")
    else:
        if player == "stone" and computer == "scissors":
            print("You Win!")
        elif player == "paper" and computer == "stone":
            print("You Win!")
        elif player == "scissors" and computer == "paper":
            print("You Win!")
        else:
            print("Computer Wins!")


game()
    
