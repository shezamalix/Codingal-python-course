try:
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    result = num1 / num2
    print(f"The division result of {num1} / {num2} = {result}")

except ValueError :
    print("ERROR ; Pls enter 2 valid numbers.")

except ZeroDivisionError :
    print("ERROR ; Pls do not enter 0 for the 2nd number.")

else:
    print("NO EXCEPTIONS OCCURED! HURRAH!")

finally:
    print("This runs no matter what! Exception/ No excpetion!")