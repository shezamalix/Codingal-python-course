str1 = "ABCDEFGHIJKL"
str2 = "2"
print(str1 + str2)
print(str1[1:])

print(str1[::3])
#START_INDEX : END_INDEX (NOT INCLUDED) : SKIP/DIRECTION
text = "Today is a sunny day."
reversedText = text[::-1]
print(reversedText)

friends = "Alice,Bob,Carol,Delilah,Elijah,Fatima"
friends_list = friends.split(",")
print(friends_list)
print(type(friends_list))
print(len(friends_list))