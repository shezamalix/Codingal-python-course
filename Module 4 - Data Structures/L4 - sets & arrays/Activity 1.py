x = {1,1,2,3,4,4,4,5}
print(x)
print(len(x))

l = list(x)
print(l)

l.append(1)
l.append(1)
l.append(1)
print(l)

l = set(l)
print(l)

#cant use append for a set

x.add(6)
print(x)

fruits = {"apple", "banana", "orange","grapes"}
other_fruits = {"apple", "dragonfruit","watermelon", "orange"}

print(fruits)

fruits.pop() # no such thing as an order in a set

print(fruits)

dict1 = {
    "a" : 1,
    "a" : 2,
    "a" : 99,
    "a" : 67
    }

print(dict1)#dictionary is a way to retain/mantain unique keys

common_fruits = fruits.intersection(other_fruits)
all_fruits = fruits.union(other_fruits)

print(common_fruits)
print(all_fruits)

difference = fruits.union(other_fruits) - fruits.intersection(other_fruits)
print(difference) #also called semmetirc difference



