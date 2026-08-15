#reverse a string using a for loop
sentence = input("Enter a word/sentence :")
reverse = ""
for i in sentence :
    print(i)
    reverse = i + reverse
print(reverse)