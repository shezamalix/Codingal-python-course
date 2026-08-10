# ACTIVITY 2: Calculate student's grade from total marks

#

# Take input of total marks

#

# If marks greater than/equal to 90, A+

# If marks greater than/equal to 80 but less than 90, grade is A

# If marks greater than/equal to 70 but less than 80, grade is B

# If marks greater than/equal to 60 but less than 70, grade is C

# If marks greater than/equal to 50 but less than 60, grade is D

# If marks greater than/equal to 40 but less than 50, grade is E

# If marks less than 40, grade is F

marks = float(input("How many marks did you get?"))

rounded_marks = int(marks)

if rounded_marks in range(90,101) :
    print("A+")
elif rounded_marks in range(80,91) :
    print("A")
elif rounded_marks in range(70,81) :
    print("B")
elif rounded_marks in range(60,71) :
    print("C")
elif rounded_marks in range(50,61) :
    print("D")
elif rounded_marks in range(40,51) :
    print("E")
else:
    print("F")
