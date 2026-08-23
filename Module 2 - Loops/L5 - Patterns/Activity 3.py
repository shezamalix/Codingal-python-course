rows = int(input("How many rows are there? "))

emoji = "😀"


for r in range(1,rows + 1):
    #line 8 =  loop for spaces
    for s in range(rows - r) :
        print(end = "   ")

    #line 12 = emoji loop
    for i in range(r):
        print(emoji, end = " ")

    print()