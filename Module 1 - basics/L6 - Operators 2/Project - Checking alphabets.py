# I was unsure on how to complete this project so I used gemini to understand what I had to do

user_input = input("Enter a character : ")

if len(user_input) == 1 and user_input.isalpha() :
    print(f"{user_input} is an alphabet")

else :
    print(f"{user_input} is not an alphabet")