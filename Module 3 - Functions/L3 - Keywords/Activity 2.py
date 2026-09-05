# Write a for loop over a range of numbers: only print the odd numbers, skip the even numbers

n = int(input("Enter a number : "))

for i in range(1,n+1) :
    if i % 2 == 0 :
        continue #only works inside inside a loop

    print(i)

var = 10 #initialise

while var > 0: #iterate loop

    var = var - 1

    if var == 5: #condition 1

        continue #continue statement

    #display result

    print ('\nCurrent variable value :', var)

print ("\nGood bye!")