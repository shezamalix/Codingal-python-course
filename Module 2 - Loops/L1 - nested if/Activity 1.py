# M2 L1 A1

# ACTIVITY 1: STUDENT CAN TAKE EXAM UNDER TWO CONDITIONS:

# Take the required input for attendance

# - Student should have attendance >= 75%

# - Check if attendance matches above criteria

# - Then Print "Allowed"

# - If attendance is low, Student should have a medical certificate

# - Take input for medical certificate

# - Check if student replied Yes or No

# - If Yes, Print "Allowed"

# - Else No, Print "Not Allowed"

attendance = float(input("Enter your attendance score :"))

if attendance >= 75 :
    print("Allowed") 

else :
    med_cert = input("Do you have a medical certificate? Enter yes or no? ")
    if med_cert == "yes":
        print("Allowed")
    else:
        print("Not allowed")

