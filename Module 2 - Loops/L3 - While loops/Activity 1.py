#Find the sum of the 1st n postitive integers
# whatever you can do with a for loop can be done with a while
#for loop is used when I know exactly how many times I want to repeat smth
#while loop is used when I dont know exactly how many times I want to repeat smth

n = int(input("Enter a number :"))

sum = 0

# Want to give Sheza 1 game at a time and stop when she has 5
# LOOP VARIABLE(the variable that the while loop is dependent on) - initial value of 1
i = 1

while i <= n:
    print(i)
    sum += i
    i += 1   #updating the loop variable by 1 in each interation
print(f"sum of the first {n} numbers = {sum}")