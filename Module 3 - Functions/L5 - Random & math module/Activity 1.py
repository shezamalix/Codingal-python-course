import random

secret_number = random.randint(1,10)

print("Guess the secret number between 1 and 100. \n The game ends when you guess it right ")

while True :
    guess = int(input("Guess a number : "))
    if guess == secret_number :
        print("You have guessed correctly")
        break
    else: 
        print("Wrong,try again! ")

# implement a hint system later on,calculating the difference between the secret number and the user guess, or by using range
