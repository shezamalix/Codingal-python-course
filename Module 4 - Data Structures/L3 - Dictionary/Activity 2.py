marks = {
    "student_1" : 100,
    "student_2" : 99,
    "student_3" : 100,
    "student_4" : 70,
    "student_5" : 86,
    
}
count = 0
for k in marks :
    print(k)#prints keys
    if marks[k] == 100:
        print("Congrats!")
        count += 1
print(count)




