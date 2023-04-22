# Compute Body Mass Index
#prompt user to enter weight
weight = eval(input("Please enter your weight in pounds/lbs: "))
#prompt user to enter height
height =  eval(input("Please enter your height in inches: "))
#conversion
kilogramsPerPound = 0.45359237 #constant
metersPerInch = 0.0254 # constant
#bmi calculation
weightInKg = weight * kilogramsPerPound
heightInMeters = height * metersPerInch
bmi = weightInKg / (heightInMeters * heightInMeters)
print("Your BMI = ", bmi)
if bmi <= 18.5:
    print("Classification: Underweight")
elif bmi <= 25:
    print("Classification: Normal")
elif bmi <= 30:
    print("Classification: Overweight")
else:
    print("Classification: Obese")
