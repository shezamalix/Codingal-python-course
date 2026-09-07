
num =  None # initial value

while not isinstance(num, int): #checks if the number is an int or not
    try :
        num = int(input("Enter a number : "))
        print(f"the user entered {num}")

    except ValueError as err : #specifically catching the value error
        print("ERROR : Please enter a valid number, don't type letters/symbols")
        