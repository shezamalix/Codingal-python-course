marks_math = 99
marks_french = 99
marks_english = 100
marks_science = 99

total_marks = 0

total_marks += marks_math
total_marks += marks_french
total_marks += marks_english
total_marks += marks_science


print("Total marks:", total_marks)

# 85%
class_average = 85


marks_achievable = 100 * 4
my_percentage = (total_marks / marks_achievable) * 100

print("Am I below class average?",class_average > my_percentage )
print("Am I average?", class_average == my_percentage)
print("Am I above average?", class_average < my_percentage)

