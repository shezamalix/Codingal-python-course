empty_list = []
print(empty_list)
print(type(empty_list))

numbers = [1,2,3,4,5,10,5,5] #every number is an element
print(numbers)
print(len(numbers))

print(numbers[0]) #1st element(at 0 index)
print(numbers[3])

print(numbers[-1])# -1 will give you the last element of a list

numbers.reverse()# permanently reverses list of elements
print(numbers)

print(min(numbers), max(numbers))

print(numbers.count(5))#shows how many times 5 occurs in the list

numbers.append(123) #adds an element to the end of the list
print(numbers)

numbers.pop()#removes the lsat element from list
print(numbers)

list1 = [3,6,9] * 3 # repeats list 3 times
print(list1)