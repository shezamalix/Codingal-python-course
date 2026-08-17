#Take 2 inputs; 1. sentence 2. character
#find out how many times the charcter appears in the sentence

sentence = input("Enter a sentence - ")
character = input("Enter a character - ")
# Hi I am sheza  character = i
i = 0
count = 0
while i < len(sentence):
    if character == sentence[i]:
        count += 1

    i += 1
print(f"{character} appeared {count} times")

