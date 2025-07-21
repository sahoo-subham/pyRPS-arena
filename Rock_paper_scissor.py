import random

user_win = 0
computer_win = 0

options = ["rock","paper","scissor"]

while True:
    user_pick = input("Type Rock/Paper/Scissor or q to Quit:").lower()

    if user_pick == "q":
        break
    if user_pick == "scissors":
        user_pick = "scissor"
    if user_pick not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    
    print("\nComputer picked:",computer_pick)

    if user_pick == "rock" and computer_pick == "scissor" :
        print("You won!")
        user_win += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_win += 1

    elif user_pick == "scissor" and computer_pick == "paper":
        print("You won!")
        user_win += 1

    elif user_pick == computer_pick:
        print("Draw")
    else:
        print("You lost!")
        computer_win += 1


print("\nFinal Score:")
print("You won",user_win,"times")
print("Computer won",computer_win,"times")

if user_win > computer_win:
    print("🎖️ 🫅 You won the game!")
elif computer_win > user_win:
    print("💻 Computer won the game!")
else:
    print("🤝 Its a tie overall!")