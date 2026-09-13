words = ["abc", "tnt", "xyz", "cfc", "12321"]

#AIM : find the number of strings where the 1st and last character are the same
#CREATE a new list out of those strings

count = 0 #count how many words match condition
result_list = []


for w in words:
    if w[0] == w[-1] :
        count += 1
        result_list.append(w)

print("Number of strings matching the requirement = ",count)
print(result_list)

#i = 0
#while i < len(words) :
 #   print(words[i])
  #  i += 1