#find if a given tuple is a palindrome or not
#cant use reverse function for a tuple
# print(details[2:4])#print the 1st 2 elements

numbers = ( 1, 2, 2, 1)

half = len(numbers) // 2

first_half = numbers[0:half]
second_half = numbers[half + len(numbers) % 2:]
print(first_half, second_half)

reversed_second_half = second_half[::-1]

if (first_half) == reversed_second_half :
    print("palindrome")

else:
    print("not a palindrome")