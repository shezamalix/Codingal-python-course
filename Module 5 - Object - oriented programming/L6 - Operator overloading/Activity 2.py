class flashcard:
    def __init___(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):

        #we will return a string
        return self.word+' ('+self.meaning+')'
flash = []
print("Welcome to flashcard application")
#the following loop will be repeated until
#userstop to add the flashcards
while(True):
    word = input("enter the name you want to add to flashcard :")
    meaning = input("Enter the meaning of the word : ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0, if you want to add another flashcard otherwise enter1 : "))

    if(option):
        break
#printing all the flashcards
print("\nYour flashcards")
for i in flash:
    print(">", i)