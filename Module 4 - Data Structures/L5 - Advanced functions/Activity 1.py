#filter out items starting with p

items = ["pencil", "eraser", "ruler", "protractor"]
    # p_items = []

    # for item in items :
    #     if item[0] == "p" :
    #         p_items.append(item)

    # print(p_items)

#instead:

#LIST COMPREHENSION - 1 LINER SHORT-CUT TO PERFORM FILTERING

#3 parts inside the square bracket
#1. what you want to add in the list
#2.What are you looping over(string,list or tuple?)
p_items = [item for item in items if item[0] == "p"]
print(p_items)

p_items = [item for item in items if item[-1] == "r"]
print(p_items)

#DICTIONARY COMPREHENSION

stock_counts = [100, 300, 87, 99]

#pencil = 100
#eraser = 300
#ruler = 87
#protractor = 99

#loop over 2 lists of the SAME SIZEEE at the same time
for item, stock in zip(items,stock_counts):
    print(item,stock)

zipped =  zip(items,stock_counts)
print(list(zipped))

#DICTIONARY COMPREHENSION

inventory = {item : stock for item,stock in zip(items,stock_counts)}
print(inventory)

#--------------------------------------------------------

numbers = [1,2,3,4,5]
#Square every number in the list and create a new list out of it
squares = []
for i in numbers:
   squares.append(i ** 2)
print(squares)

#or:

squares = [i ** 2 for i in numbers]
print(squares)

#MAP FUNCTION - To transform an exisitng list to something else
# 1 LINER FUNCTIONS = LAMBDA
squares = map(
    lambda n:n ** 3, #n is every element in the numbers list
    numbers
)

print(list(squares))






   









    