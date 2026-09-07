recorded_age = 15
entered_age = int(input("Enter your age : "))

try:
    if recorded_age == entered_age :
        print("You have entered the correct age")

except ValueError:
    print("Please enter your truthful age")