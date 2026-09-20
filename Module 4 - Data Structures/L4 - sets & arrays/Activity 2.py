import array as arr # alias - nickname/short form of original name

#arrays:
#1 . contiguous list - its stored right 1 after the other in memory
#2 . you can store only similiar data types in an array

arr1 = arr.array("i", [10, 45, 990])

print(arr1)

arr2 = arr.array('f', [1.5, 4.9, 3.14])

print(arr2)

arr1.append(54)
print(arr1)

arr1.reverse()
print(arr1)

arr1.insert(3, 111)#adds before the index u give it
print(arr1)

