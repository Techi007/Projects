# BMI Calculator

# Concept: Ask the user for their weight and height, then calculate their Body Mass Index (BMI)
# using the formula BMI = weight / height^2.

# Weight: in lbs 
# height: in inches

weight = float(input("Weight: "))
height = float(input("Height: "))

bmi = (weight * 703) / (height ** 2)
print("")

print(f"BMI: {bmi:.2f}")