#find the number of digits in the given integer
#find the sum of the digits using a while loop

num = 3498

while num > 0 :
    print(num % 10)

#update loop variable by floor dividing by 10
    num //= 10

# % 10 gives us the last digit in the number