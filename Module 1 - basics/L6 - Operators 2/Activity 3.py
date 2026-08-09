# 1) Ask the user to enter their height in centimeters and store it in `height`.
height = int(input("Enter your  height in cm:"))
# 2) Ask the user to enter their weight in kilograms and store it in `weight`.
weight = int(input("Enter your weight in kg : "))
# 3) Calculate BMI using the formula:

# BMI = weight ÷ (height in meters)²
BMI = weight / (height / 100)**2
# (Convert height from cm to meters by dividing by 100.)

# Store the result in `BMI`.

# 4) Print the BMI value.

# 5) Use if–elif–else to decide the BMI category:

# - If BMI is 18.4 or less → print "underweight"
if BMI <= 18.4 :
    print("underweight")
# - Else if BMI is 24.9 or less → print "healthy"
elif BMI <= 24.9 :
    print("healthy")
# - Else if BMI is 29.9 or less → print "over weight"
elif BMI <= 29.9 :
    print("overweight")
# - Else if BMI is 34.9 or less → print "severely over weight"
elif BMI <= 34.9 :
    print("severly overweight")
# - Else if BMI is 39.9 or less → print "obese"
elif BMI <= 39.9 :
    print("obese")
# - Else → print "severely obese"if BMI <= 18.4 :
else:
    print("severly obese")