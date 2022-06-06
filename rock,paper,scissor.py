import random

User_wins = 0
Pc_wins= 0
games = range(int(input("How many times do you wanna play? ")))

for z in games:
    pc = random.choice(["rock", "paper", "scissor"])
    print("\nGame", z + 1)
    user = input("Do you pick Rock, Paper, or Scissor? ")

    if user.lower() == "rock":
        if pc == "rock":
            print("I got", pc + "!")
            print("It's a tie!")
        elif pc == "paper":
            print("I got", pc + "!")
            print("You lose!")
            Pc_wins += 1
        else:
            print("I got", pc + "!")
            print("You win!")
            User_wins += 1
    elif user.lower() == "paper":
        if pc == "paper":
            print("I got", pc + "!")
            print("It's a tie!")
        elif pc == "scissor":
            print("I got", pc +"!")
            print("You lose!")
            Pc_wins += 1
        else:
            print("I got", pc + "!")
            print("You win!")
            User_wins += 1
    elif user.lower() == "scissor":
        if pc == "scissor":
            print("I got", pc + "!")
            print("It's a tie!")
        elif pc == "rock":
            print("I got", pc + "!")
            print("You lose!")
            Pc_wins += 1
        else:
            print("I got", pc + "!")
            print("You win!")
            User_wins += 1
    else:
        print("Not a valid answer")

print("The score is", User_wins, "-", Pc_wins)
if User_wins > Pc_wins:
    print("You win!")
elif User_wins < Pc_wins:
    print("You lose!")
else:
    print("Its a tie!")
