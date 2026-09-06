# M3 L3 Assignment:

#Write a program to satisfy the following conditions of the given range:

#put the entire thing in a function with an arguement upto which the for loop should run

# #If the number is divisible by 20, it provides an output "twist."

#If the number is divisible by 15, it will pass (no output)

#If the number is divisible by 5, it will give an output “fizz.”

#If the number is divisible by 3, it will give an output "buzz."

#Otherwise, it will give the output of that number.

def num(upto):
    for number in range(1, upto + 1):

        if number % 20 == 0:
            print("twist")

        elif number % 15 == 0:
            pass

        elif number % 5 == 0:
            print("fizz")

        elif number % 3 == 0:
            print("buzz")

        else:
            print(number)


user_input = int(input("Enter a number: "))
num(user_input)
