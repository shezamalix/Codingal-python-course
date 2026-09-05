# 1) Take a word input from the user and store it in `a`.

# 2) Use a `for` loop to iterate through each character `i` in the word `a`.
# 3) For each character, check if it is equal to 'A':
#    a) If `i == 'A'`, print "A is found".
#    b) Use `break` to stop the loop immediately after finding 'A'.

# 4) If the current character is not 'A', print "A not found".
#    (This message prints for each character until 'A' is found or the loop ends.)


word = input("Enter a word : ")

for i in word : 
    if i == "A" :
        print("A is found")
        break
    #break(completley stops loop from going further) is always used inside a for/while loop ,gives an error if used anywhere else
    else :
        print("A is not found")
