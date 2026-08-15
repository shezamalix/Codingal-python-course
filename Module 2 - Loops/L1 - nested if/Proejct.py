# Take a integer input from user

# If it is a multiple of 3, print "Fizz" instead of the number.

# If it is a multiple of 5, print "Buzz" instead of the number.

# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

integer = int(input("Enter a number :"))

if integer % 3 == 0 and integer % 5 == 0:
    print("FizzBuzz")
elif integer % 3 == 0:
    print("Fizz")

elif integer % 5 == 0:
    print("Buzz")