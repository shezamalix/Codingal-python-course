# ROCK PAPER SCISSORS
# Step 1 : Computer chooses a random option between Rock, Paper, Scissors
# Step 2 : Input from the user for their option
# Step 3 : Decide who won
# Step 4 : Stop after 5 turns & declare winner


import random

p_score = 0
c_score = 0
turn = 1

while turn <= 5:
    print("--- Turn", turn, "---")
    
    comp = random.choice(["rock", "paper", "scissors"])
    user = input("Choose rock, paper, or scissors: ")
    
    print("Computer chose:", comp)
    
    if user == comp:
        print("Tie!\n")
    elif user == "rock" and comp == "scissors":
        print("You win!\n")
        p_score += 1
    elif user == "paper" and comp == "rock":
        print("You win!\n")
        p_score += 1
    elif user == "scissors" and comp == "paper":
        print("You win!\n")
        p_score += 1
    else:
        print("Computer wins!\n")
        c_score += 1
        
    turn += 1

print("Final Score - You:", p_score, "Computer:", c_score)

if p_score > c_score:
    print("You won the game!")
elif c_score > p_score:
    print("Computer won the game!")
else:
    print("It's a tie game!")