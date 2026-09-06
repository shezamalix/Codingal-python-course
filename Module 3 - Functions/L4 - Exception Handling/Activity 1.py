#print("Sheza")
# print("Sheza")
# print("Sheza")
# print("Sheza")
# print("Sheza")
# a = b

#code doesnt run at all if there is a syntax error
#exceptions - if there any other error(name error), the code will run up until the error occurs or an error that stops a program

#ValueError
#try need indentation
#try will attempt to run the code inside it 
#and the control will pass to the "except" block if an error occurs
try : 
    num = int(input("Enter a number : "))
    print(f"the user entered {num}")
#err is a variable which could be anything
# "as err" is used to check what the error message actually is
except ValueError as err : #specifically catching the value error
    print("Please enter a valid number, don't type letters/symbols")
    print(err)