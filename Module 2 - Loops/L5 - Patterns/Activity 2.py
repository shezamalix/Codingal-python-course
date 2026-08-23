rows = int(input("How many rows are there? "))

emoji = "😀"


for r in range(1,rows + 1):
    print(r)
    for i in range(r):
        print(emoji, end = " ")

    print()