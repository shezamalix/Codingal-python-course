#find out wether the input is a prime number or not

user_input = int(input("Enter a number :")) 

for factor in range(2,user_input) :
    if user_input % factor == 0:
        print(f"{user_input} is not a prime number")
        break #stops the loop
else:
    #else block for a loop runs when the loop has not broken at all
    print(f"{user_input} is a prime number")
