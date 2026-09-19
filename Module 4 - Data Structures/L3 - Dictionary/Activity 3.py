#Dictionary of students (id -> details)
student_data = {
"id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
"id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
"id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
"id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},

}

 #TASK : Create a new dictionary with unique students only(no duplicates)

result = {}
unique_students = []
for student_id,details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])
    #print(unique_key)

    if unique_key not in unique_students :
        unique_students.append(unique_key)
        result[student_id] = details

print(result)