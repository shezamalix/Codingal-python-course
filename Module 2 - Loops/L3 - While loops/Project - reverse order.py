# I used ai to help me with this project

number_text = input("Enter a number: ")
count = 0
index = 0

if number_text[0] == "-":
    index = 1

while index < len(number_text):
    count = count + 1
    index = index + 1 

print("Number of digits:", count)