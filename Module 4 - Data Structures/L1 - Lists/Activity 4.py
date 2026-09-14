names = ["Sheza", "Omer", "Abishek", "Sam"]

def find(lst, target):
#for loops and if statements
    index = 0
    for i in lst:
      if target == i :
         return index

      index += 1

    return -1
    

        
    
      

#return the index of target inside the list l and if the target is not found,return -1


print(find(names, "Sheza"))#should return 0
print(find(names, "Omer"))#return 1
print(find(names, "Dan"))# -1