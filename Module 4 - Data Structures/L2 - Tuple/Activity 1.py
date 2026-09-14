#Immutable data structure - tuple
#Means you cant change the individual elements once it has been created

t = (10, 20, 30)
print(type(t))

print(t[-1])

print(len(t))

#t[0] = 40

s = (40, 50, 60)

#line 16 works for a list aswell and creates a whole new tuple
t = t + s
print(t)

#suggestion : tuples are "usually" used for heterogeneous data(all elements represent different things)

details = ("Sheza", 10, "Pasta", 155.5)
print(details.count("Pasta"))

print(details[2:4])#print the 1st 2 elements